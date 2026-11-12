# Glossary

- **Action:** operation such as `count` or `write` that executes a Spark plan.
- **AQE:** Adaptive Query Execution; Spark adjusts some choices using runtime statistics.
- **Bronze/Silver/Gold:** raw/auditable, cleaned/conformed, and consumer-ready layers.
- **Catalog / schema:** Unity Catalog namespaces: `catalog.schema.table`.
- **Delta transaction log:** ordered metadata files that make table commits reliable and versioned.
- **Driver / executor:** planner process / worker processes that run tasks.
- **Lazy evaluation:** Spark delays computation until an action.
- **Partition:** a slice of a distributed dataset processed by a task.
- **Shuffle:** redistribution of records across partitions, often for joins or aggregations.
- **Watermark:** a streaming rule for how long to wait for late events.
