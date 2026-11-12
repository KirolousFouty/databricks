# Spark execution

Transformations create a logical plan. At an action, Catalyst optimizes it, Spark constructs physical stages, and scheduler tasks process partitions on executors. Narrow transformations can stay within a partition; wide ones (many joins, `groupBy`, `distinct`) usually shuffle. Inspect `explain()` rather than guessing.
