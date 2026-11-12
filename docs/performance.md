# Performance guide

Start with correctness and plans. Filter/select early, avoid Python UDFs, broadcast only small dimensions, choose partitioning based on data and downstream reads, and watch for skew and many tiny files. Cache only reused, expensive intermediates and unpersist them. Tiny lab data is not evidence for production tuning.
