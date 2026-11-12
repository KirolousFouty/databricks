# Setup

## Local Jupyter mode

Install Python 3.9–3.11 and Java 17. Create a virtual environment, install `requirements.txt`, set `PYTHONPATH=src`, generate `data/raw`, and launch Jupyter as shown in the README. The core notebooks use local PySpark. Small data proves correctness, not benchmark performance.

## Databricks mode

Import the repo or use it as a Git folder. Choose a supported Databricks Runtime with Python and Spark; the runtime bundles its own compatible Delta implementation, so do not blindly pip-install the local pins into a cluster. Attach a notebook, configure approved Unity Catalog storage, and start at notebook 00. Cluster/serverless availability, Unity Catalog access, volumes, Auto Loader, and Jobs permissions depend on workspace edition, cloud, and administrator policy.

## Compatibility

| Component | Local baseline | Databricks |
| --- | --- | --- |
| Python | 3.9–3.11 | Runtime-provided |
| Spark | PySpark 3.5.3 | Runtime-provided |
| Delta | delta-spark 3.2.0, compatible Spark | Runtime-provided Delta |
| Java | 17 recommended | Managed |

Use `spark.version` to inspect the active runtime. Keep Spark and Delta versions matched; mixed versions are a frequent source of JVM errors.
