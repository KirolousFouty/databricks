"""Locally runnable end-to-end Medallion pipeline. Delta is optional and selected by format."""
from pathlib import Path
from typing import Any
from pyspark.sql import SparkSession, functions as F
from .transformations.silver import clean_orders, clean_products
from .transformations.gold import daily_revenue, product_performance, customer_lifetime_value

def run_pipeline(spark: SparkSession, raw_dir: str | Path, output_dir: str | Path, fmt: str = "parquet") -> dict[str, Any]:
    raw, out = str(raw_dir), Path(output_dir)
    orders = spark.read.option("header", True).csv(f"{raw}/orders.csv")
    items = spark.read.option("header", True).csv(f"{raw}/order_items.csv").withColumn("quantity", F.col("quantity").cast("int")).withColumn("unit_price", F.col("unit_price").cast("decimal(12,2)"))
    products = spark.read.option("header", True).csv(f"{raw}/products.csv")
    bronze = orders.withColumn("_ingested_at", F.current_timestamp()).withColumn("_source_file", F.input_file_name())
    bronze.write.mode("overwrite").format(fmt).save(str(out / "bronze_orders"))
    silver_orders, silver_products = clean_orders(orders), clean_products(products)
    silver_orders.write.mode("overwrite").format(fmt).save(str(out / "silver_orders"))
    results = {"daily_revenue": daily_revenue(silver_orders, items), "product_performance": product_performance(silver_orders, items, silver_products), "customer_lifetime_value": customer_lifetime_value(silver_orders, items)}
    for name, df in results.items(): df.write.mode("overwrite").format(fmt).save(str(out / f"gold_{name}"))
    return {"bronze_rows": bronze.count(), "silver_order_rows": silver_orders.count(), "gold_tables": list(results)}
