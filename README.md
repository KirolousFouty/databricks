# RetailFlow Analytics — Databricks Learning Lab

A self-contained, production-inspired course that teaches Databricks, Apache Spark, Delta Lake, governance, streaming, and orchestration by building an e-commerce analytics platform. It is for Python/SQL learners moving into data engineering.

## Start here

1. Read [SETUP.md](SETUP.md), create the environment, and generate data.
2. Open `notebooks/00_databricks_introduction.ipynb`, then work through notebooks in numeric order.
3. Attempt the exercises before opening the corresponding `solutions/` file.
4. Finish with `15_capstone_project.ipynb`.

The included data is synthetic and deterministic. It intentionally has duplicated keys, a null email, a malformed timestamp, inconsistent category spelling, an invalid price, and a malformed CSV so that quality practices are real experiments rather than prose.

## Quick start (local)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH="$PWD/src"
python -m retailflow.data_generation.generator --output data/raw
jupyter lab
pytest -q
```

Java 17 is the recommended local Spark runtime; Python 3.9–3.11 is supported by the pinned PySpark version. Delta examples need a Spark/Delta-compatible runtime; use a Databricks cluster for the most reliable Delta lesson experience.

## Project map

| Area | Purpose |
| --- | --- |
| `notebooks/` | 16 sequenced, executable lessons with experiments, exercises, and checks |
| `src/retailflow/` | generator, quality contracts, transformations, and pipeline |
| `data/sample/` | deterministic sample source data (regenerate any time) |
| `tests/` | fast generator and teaching-contract tests |
| `resources/` | deployment and workflow examples |
| `docs/` | reference explanations and diagrams |

## Databricks use

Upload/import this repository, attach notebooks to an appropriate cluster, and set `RETAILFLOW_ROOT` to a workspace-accessible project location if needed. For Unity Catalog, set `RETAILFLOW_CATALOG` and use a catalog/schema and external location approved by your administrator. Notebook 13 intentionally does not attempt grants or create governed objects. Auto Loader, Unity Catalog, job execution, serverless features, Delta `OPTIMIZE`, and managed-table administration are labeled Databricks-specific.

## Run the end-to-end baseline

The capstone runs `retailflow.pipeline.run_pipeline(spark, "data/raw", "storage")`. It writes Parquet locally by default, which preserves the lesson without pretending to be Delta. On a compatible Delta runtime, pass `fmt="delta"`. Re-running overwrites the same learning outputs, demonstrating basic idempotent behavior.

## Reset and troubleshoot

Delete only `data/raw`, `data/generated`, or `storage` (generated paths), then rerun the generator. See [TROUBLESHOOTING.md](TROUBLESHOOTING.md). Never run broad deletion commands against a workspace or cloud storage root.
