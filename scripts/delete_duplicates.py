import pandas as pd
import sys

if len(sys.argv) < 4:
    print("Not enough arguments")
    print("Usage: delete_duplicates.py [DUPLICATE_CSV] [ORIGINAL_CSV] [OUTPUT_CSV]\n")
    print("DUPLICATE_CSV: Path to CSV with rows to remove from original CSV")
    print("ORIGINAL_CSV: Path to CSV with duplicates")
    print("OUTPUT_CSV: Path to CSV to be created without duplicates")
    sys.exit()

duplicate = pd.read_csv(sys.argv[0])
all = pd.read_csv(sys.argv[1])

#find all rows without a match from duplicateBarcodes in allBarcodes
output = all[~all.column1.isin(duplicate.column1)]

noDuplicate = pd.DataFrame(output)

noDuplicate.to_csv(sys.argv[2], header = True, index = True)