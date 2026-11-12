# Solutions — 11 Performance Optimization

Use built-in Spark functions: filter invalid timestamps with `to_timestamp`, deduplicate on business keys, then aggregate after filtering `status = 'completed'`. Compare your output with the reusable functions in `src/retailflow/transformations/`.
