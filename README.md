Here is a copy-paste format README for your GitHub repository.

-----

#  BedSort

**BedSort** is a Python script that provides **custom, rule-based sorting** for genomic interval files (like **BED** format) read from standard input (`stdin`). Unlike standard lexical sorting, this tool allows you to define a specific, non-alphabetic order for chromosomes (contigs) based on a separate configuration file.

This is particularly useful in genomics pipelines where a specific chromosome order (e.g., `chr1`, `chr2`, ..., `chrX`, `chrY`, `chrM`, followed by unplaced contigs) is required for consistency or downstream tool compatibility.

##  Features

  * **Rule-Based Chromosome Sorting:** Defines the exact order of chromosomes using an external `tsv` file.
  * **Genomic Coordinates Sort:** After custom chromosome sorting, intervals are sorted by **start position** and then **end position**.
  * **Standard I/O:** Reads data from `stdin` and writes the sorted output to `stdout`, making it easy to integrate into shell pipelines.
  * **Pandas-Powered:** Efficient data handling and sorting using the `pandas` library.

##  Installation

This script requires **Python** and the **`pandas`** library.

1.  **Install `pandas`:**

    ```bash
    pip install pandas
    ```

2.  **Save the Script:**
    Save the provided Python code as a file named, for example, `bedsort.py`.

## ⚙️ Configuration: The Selection File

The custom chromosome order is defined in a **tab-separated values (TSV)** file. By default, the script looks for a file named **`standard_selection.tsv`**.

This file must contain **a single column** listing the desired chromosome names in the precise order you want them to appear in the final output.

### Example `standard_selection.tsv`:

| chrom |
| :---: |
| chr1  |
| chr2  |
| ...   |
| chr22 |
| chrX  |
| chrY  |
| chrM  |
| GL000192.1 |
| ... |

##  Usage

Run the script by piping your unsorted data (e.g., a BED file) into it.

```bash
# Assuming your unsorted file is 'unsorted.bed'
cat unsorted.bed | python bedsort.py > sorted.bed
```

### Script Breakdown:

| Step | Description |
| :--- | :--- |
| **1. Load Rulebook** | Reads `standard_selection.tsv` to establish the `custom_order`. |
| **2. Read Data** | Reads tab-separated data from `stdin` (assuming BED-like format). |
| **3. Filter** | Only keeps rows where the chromosome is present in the `custom_order`. |
| **4. Enforce Sort Order** | Converts the `chrom` column to a **CategoricalDtype** based on the `custom_order`. |
| **5. Sort** | Sorts first by the custom `chrom` order, then by `start`, then by `end`. |
| **6. Write Output** | Writes the final sorted data to `stdout` without headers or an index. |



-----

Would you like to generate an example `standard_selection.tsv` file for the human genome?
