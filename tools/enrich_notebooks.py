"""Add topic-specific executable context after base notebook generation."""
import json
from pathlib import Path

notes = {
 "01": ("Spark execution", "Partitions are independent task inputs. `groupBy`, joins, and `distinct` often shuffle rows across partitions; inspect `explain()` to see exchanges."),
 "02": ("DataFrame mechanics", "Use built-in `when`, joins, and window functions before Python UDFs. Native expressions allow predicate pushdown and whole-stage code generation."),
 "03": ("SQL equivalence", "Create a temporary view from the cleaned DataFrame, then compare a SQL aggregation with the DataFrame aggregation. They use the same optimizer."),
 "04": ("Reliable ingestion", "Explicit schemas and corrupt-record handling make failure observable. Incremental ingestion must track what was processed so retries are idempotent."),
 "05": ("Delta capabilities", "Delta transaction logs coordinate atomic commits. Schema evolution, MERGE, history, time travel, OPTIMIZE, and VACUUM must be used only on compatible runtimes."),
 "06": ("Bronze implementation", "Write raw rows with `_ingested_at` and `_source_file`; retain duplicates and malformed values as source evidence for auditability."),
 "07": ("Silver implementation", "Cast dates and numbers, standardize categories, deduplicate keys, validate relationships, and quarantine invalid rows before producing trusted entities."),
 "08": ("Gold implementation", "Compute revenue only from completed orders. Publish tables at documented grain: daily revenue, customer lifetime value, product performance, and category sales."),
 "09": ("Quality implementation", "Measure non-null, uniqueness, referential integrity, and positive-value rules. Emit a metric record and a quarantine DataFrame for every failed expectation."),
 "10": ("Advanced transformation", "Use `explode` for arrays, window functions for ranks/running values, and SCD Type 1/2 patterns to model changing dimensions."),
 "11": ("Performance practice", "Focus on scans and shuffles, not tiny local timings. Test broadcast joins only with small dimensions; inspect skew and small files in plans and metrics."),
 "12": ("Streaming reliability", "A checkpoint permits recovery. Watermarks bound state for late records. Auto Loader is optional Databricks ingestion, not a local-file substitute."),
 "13": ("Governance practice", "Use catalog.schema.table names and least privilege. Catalog administration requires permission, so this lab uses read-only examples by default."),
 "14": ("Workflow practice", "Tasks should be parameterized, retry-safe, observable, and connected by explicit dependencies. Review the bundled YAML before deployment."),
 "15": ("Capstone run", "The capstone reuses the package pipeline: generate → Bronze → Silver → Gold → verify. Local output is Parquet; Delta is a deliberate opt-in."),
}
for path in Path('notebooks').glob('*.ipynb'):
    key = path.name[:2]
    if key not in notes: continue
    nb = json.loads(path.read_text())
    heading, explanation = notes[key]
    cell = {"cell_type":"markdown", "metadata":{}, "source":[f"## {heading}\n", "\n", explanation + "\n"]}
    # Insert before exercises so each lesson has topic-specific production context.
    index = next(i for i,c in enumerate(nb['cells']) if c['cell_type']=='markdown' and '## Try It Yourself' in ''.join(c['source']))
    nb['cells'].insert(index, cell)
    path.write_text(json.dumps(nb, indent=1) + "\n")
