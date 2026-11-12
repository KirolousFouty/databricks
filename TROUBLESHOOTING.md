# Troubleshooting

| Symptom | Likely cause and safe fix |
| --- | --- |
| `ModuleNotFoundError: retailflow` | Run Jupyter from project root and export `PYTHONPATH="$PWD/src"`. |
| Java gateway exits | Install/use Java 17, restart the kernel, and ensure `JAVA_HOME` is coherent. Java 25 is not a tested PySpark target. |
| Delta class/version error | Do not mix arbitrary Spark and Delta package versions; use pinned local versions or the Databricks Runtime bundle. |
| Permission denied in UC | Ask the administrator for the catalog/schema/external-location permission; do not work around governance. |
| Streaming rerun error | Delete only the lesson's checkpoint directory after stopping the query, then restart. |
| Assertion changes after edits | This is expected in experiments—recreate data with the deterministic generator before comparing baselines. |

For a failed job, inspect the first meaningful executor/driver exception, input schema, and query plan before changing configuration.
