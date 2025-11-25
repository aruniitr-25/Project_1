#### Project 1: Quick Bed Sort (Pandas Version)

Goal: Efficiently merge, filter, and sort genomic interval data (BED files) using the Pandas library. This approach leverages vectorized operations for high performance and uses categorical data types to enforce a custom chromosome sort order.




#### Language

Python

The main script using Pandas to filter and sort the data.

standard_selection.tsv

Text

A "rulebook" file listing the chromosomes to keep, in the specific desired order.

#### Prerequisites

Python 3.x

Library: pandas

To install pandas, run:
bash
```
pip install pandas
```

#### Usage

1. Generate the Rulebook

First, ensure you have the standard_selection.tsv file which defines your sorting order.
bash
```
(echo chr{1..22} | tr ' ' '\n'; echo chrX; echo chrY) > standard_selection.tsv

```
2. Run the Script

Pipe your BED data directly into the script. This example merges two files and pipes them into the Python script.
bash 
```
cat shuf.a.bed.gz shuf.b.bed.gz | gzip -d | python3 project1.py > sorted_output.bed
```

#### Output: `sorted_output.bed `(A fully sorted BED file).
