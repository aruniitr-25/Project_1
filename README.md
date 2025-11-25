Project 1: Quick Bed Sort (Pandas Version)

Goal: Efficiently merge, filter, and sort genomic interval data (BED files) using the Pandas library. This approach leverages vectorized operations for high performance and uses categorical data types to enforce a custom chromosome sort order.

 Key Features

Data Science Approach: Uses pandas to treat genomic data as structured DataFrames, making the code concise and highly readable.

Custom Sorting: Utilizes Pandas CategoricalDtype to enforce a strict, user-defined chromosome order (e.g., chr1, chr2... chrX, chrY).

Secondary Sorting: Automatically handles multi-column sorting (Chromosome $\rightarrow$ Start $\rightarrow$ End) in a single optimized function call.

Robust Parsing: Handles standard tab-separated values and automatically skips comments or malformed headers.

 File Structure

File

Language

Description

project1.py

Python

The main script using Pandas to filter and sort the data.

standard_selection.tsv

Text

A "rulebook" file listing the chromosomes to keep, in the specific desired order.

🛠 Prerequisites

Python 3.x

Library: pandas

To install pandas, run:

pip install pandas


 Usage

1. Generate the Rulebook

First, ensure you have the standard_selection.tsv file which defines your sorting order.

(echo chr{1..22} | tr ' ' '\n'; echo chrX; echo chrY) > standard_selection.tsv


2. Run the Script

Pipe your BED data directly into the script. This example merges two files and pipes them into the Python script.

cat shuf.a.bed.gz shuf.b.bed.gz | gzip -d | python3 project1.py > sorted_output.bed


(Note: gzip -d decompresses the stream before it hits Python, or you can modify the script to handle gzip input directly.)

Output: sorted_output.bed (A fully sorted BED file).
