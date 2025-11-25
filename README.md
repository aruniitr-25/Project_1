# README — BED File Custom Chromosome Sorter

This script sorts BED-like genomic interval files using a **custom chromosome order** provided in a rulebook file (`standard_selection.tsv`).  
It reads BED data from **STDIN** and writes sorted output to **STDOUT**, making it ideal for use in Unix pipelines.

---

## Features
- Reads custom chromosome order from a file (`standard_selection.tsv`)
- Accepts BED/TSV data from STDIN
- Filters out chromosomes not present in the rulebook
- Sorts by:
  1. Chromosome (custom order)
  2. Start position
  3. End position
- Outputs TSV to STDOUT with no header

---

## Required Files

### 1. standard_selection.tsv
A single-column file listing chromosome names in the desired order:


