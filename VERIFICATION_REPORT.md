# Verification report

Date: 2026-11-12

## Passed

- Generated `data/sample/` using the deterministic seed: 31 customer rows, 15 products, 91 order rows, 175 order items, and 150 website events.
- Ran `pytest -q`: **2 passed**.
- Ran `python3 -m compileall -q src tools`: passed.
- Parsed all 16 notebook JSON files with Python's JSON parser.
- Verified every notebook has nbformat 4, at least 10 cells, and the required Learning Objectives, Try It Yourself, Exercises, and Knowledge Check sections.
- Checked the repository for placeholder/TODO markers in the course sources: none found.

## Not run / limitations

- PySpark and nbformat were not installed in the supplied environment. An attempt to install the pinned PySpark dependency began downloading the 317 MB distribution but did not complete during this session.
- The host Java is 25; the project documents Java 17 as its tested local target. Therefore no Spark session, local notebook execution, integration pipeline run, Delta operation, or lint run was claimed as successful.
- Databricks-only functions (Unity Catalog permissions, Jobs execution, Auto Loader, Delta managed operations, and serverless compute) need a configured Databricks workspace and were intentionally not attempted.

## Recommended follow-up verification

On a machine with Java 17, run `pip install -r requirements.txt`, then `PYTHONPATH=src pytest -q`; execute notebooks 00–15 in order; and run the capstone's Parquet baseline. On Databricks, repeat Delta-specific cells using an approved runtime and Unity Catalog location.
