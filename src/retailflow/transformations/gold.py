"""Gold metrics based on completed orders only—an explicit business-rule decision."""
from typing import Any
from pyspark.sql import functions as F

def _sales(orders: Any, items: Any) -> Any:
    return orders.filter(F.col("status") == "completed").join(items, "order_id").withColumn("revenue", F.col("quantity") * F.col("unit_price"))
def daily_revenue(orders: Any, items: Any) -> Any:
    return _sales(orders, items).groupBy(F.to_date("order_ts").alias("order_date")).agg(F.round(F.sum("revenue"), 2).alias("revenue"), F.countDistinct("order_id").alias("orders")).orderBy("order_date")
def product_performance(orders: Any, items: Any, products: Any) -> Any:
    return _sales(orders, items).join(products, "product_id").groupBy("product_id", "product_name", "category").agg(F.round(F.sum("revenue"),2).alias("revenue"), F.sum("quantity").alias("units_sold")).orderBy(F.desc("revenue"))
def customer_lifetime_value(orders: Any, items: Any) -> Any:
    return _sales(orders, items).groupBy("customer_id").agg(F.round(F.sum("revenue"),2).alias("lifetime_value"), F.countDistinct("order_id").alias("completed_orders")).orderBy(F.desc("lifetime_value"))
