# Delta Lake

Delta records atomic commits in `_delta_log`, enabling consistent reads, schema controls, history, and commands such as `MERGE`. Parquet alone is a file format, not a transactional table protocol. Time travel, `MERGE`, `UPDATE`, and `DELETE` require a compatible Delta runtime. Databricks adds managed operations such as optimized writes and `OPTIMIZE`; check edition/runtime documentation before using them.
