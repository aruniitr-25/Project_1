import sys
import pandas as pd

# --- CONFIGURATION ---
SELECTION_FILE = "standard_selection.tsv"

def main():
    # 1. Load the Rulebook (Selection File)
    try:
        # Read the single column of chromosome names
        rules_df = pd.read_csv(SELECTION_FILE, header=None, names=["chrom"])
        # Convert to a list to define the specific sort order
        custom_order = rules_df["chrom"].tolist()
    except FileNotFoundError:
        sys.stderr.write(f"Error: {SELECTION_FILE} not found.\n")
        sys.exit(1)

    # 2. Read the Data from Stdin
    try:
        # We read the tab-separated data. 
        # We assume at least 3 columns: chrom, start, end.
        # We set header=None because BED files usually don't have headers.
        # We set usecols=[0, 1, 2] to ensure we get the essentials, 
        # but reading the whole line is better to preserve extra data.
        df = pd.read_csv(sys.stdin, sep="\t", header=None, comment='#', dtype={0: str, 1: int, 2: int})
    except pd.errors.EmptyDataError:
        # If input is empty, just exit silently
        sys.exit(0)

    # 3. Rename columns for clarity (assuming standard BED format)
    # If there are more columns, we just rename the first 3
    df.rename(columns={0: "chrom", 1: "start", 2: "end"}, inplace=True)

    # 4. Filter: Keep only chromosomes in our rulebook
    df = df[df["chrom"].isin(custom_order)]

    # 5. The "Magic" Step: Enforce Custom Sort Order
    # We tell Pandas that 'chrom' is a category with a specific order (our rulebook)
    df["chrom"] = df["chrom"].astype(pd.CategoricalDtype(categories=custom_order, ordered=True))

    # 6. Sort: First by Chromosome (custom), then by Start, then by End
    df_sorted = df.sort_values(by=["chrom", "start", "end"])

    # 7. Write to Stdout
    df_sorted.to_csv(sys.stdout, sep="\t", index=False, header=False)

if __name__ == "__main__":
    main()