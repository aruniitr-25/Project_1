Project 2: Rescale to Reference

Goal: Correct the fragment length bias in a query dataset by statistically resampling it to match a "perfect" reference distribution. This pipeline removes "noise" (short fragment peaks) while retaining signal (nucleosome peaks) using a probabilistic rejection sampling method.

Key Features

Hybrid Pipeline: Combines the speed of Bash/Awk for text processing with the logic of Python for statistical calculation.

Memory Efficient: Uses stream processing (pipes) to handle millions of genomic records without loading the whole file into RAM.

Probabilistic Sampling: Implements a "Keep Probability" rule for every fragment length ($0$ to $1.0$) rather than simple hard thresholds.
