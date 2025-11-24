import csv

# Input and output file names
input_file = 'geniiAggregateSortFreq.csv'
output_file = 'geniiTotalByAlpha.csv'

# Read the CSV file
with open(input_file, 'r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    data = list(reader)

# Sort the data alphabetically by the 'name' column (case-insensitive)
data.sort(key=lambda x: x['name'].lower())

# Write the sorted data to the output file, excluding the 'frequency' column
with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    fieldnames = ['name', 'field']  # Only include name and field
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow({'name': row['name'], 'field': row['field']})

print(f"Sorted CSV written to {output_file}")