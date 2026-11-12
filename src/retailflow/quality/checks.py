"""Small Spark-native quality checks that return metrics instead of hiding failures."""
from typing import Any

def check_not_null(df: Any, column: str) -> dict[str, Any]:
    failures = df.filter(df[column].isNull()).count()
    return {"check": f"{column} not null", "passed": failures == 0, "failures": failures}

def check_unique(df: Any, column: str) -> dict[str, Any]:
    failures = df.groupBy(column).count().filter("count > 1").count()
    return {"check": f"{column} unique", "passed": failures == 0, "failures": failures}

def check_positive(df: Any, column: str) -> dict[str, Any]:
    failures = df.filter(df[column] <= 0).count()
    return {"check": f"{column} positive", "passed": failures == 0, "failures": failures}
