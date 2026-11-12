"""Reusable Silver transformations; callers provide DataFrames so storage stays configurable."""
from typing import Any
from pyspark.sql import functions as F

def clean_orders(orders: Any) -> Any:
    return (orders.withColumn("order_ts", F.to_timestamp("order_timestamp"))
        .filter(F.col("order_ts").isNotNull())
        .dropDuplicates(["order_id"])
        .withColumn("status", F.lower(F.trim("status"))))

def clean_products(products: Any) -> Any:
    return (products.withColumn("unit_price", F.col("unit_price").cast("decimal(12,2)"))
        .withColumn("category", F.initcap(F.trim("category")))
        .filter(F.col("unit_price").isNotNull())
        .dropDuplicates(["product_id"]))
