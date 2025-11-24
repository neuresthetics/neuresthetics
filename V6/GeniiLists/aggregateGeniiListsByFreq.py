import csv
from collections import defaultdict, Counter
import difflib
import re

# List of source files
file_names = ['geniiGrok.csv', 'geniiGemini.csv', 'geniiDeepSeek.csv', 'geniiGPT.csv']

# Step 1: Parse all source CSVs
all_entries = []
for fn in file_names:
    with open(fn, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            all_entries.append({'name': row['name'], 'field': row['field'].lower(), 'source': fn})

# Normalization function
def normalize_name(name):
    name = name.lower()
    name = re.sub(r'[^a-z\s]', '', name)  # Remove non-letters except spaces
    words = name.split()
    words.sort()
    return ' '.join(words)

# Step 2: Normalize and group
normalized_to_originals = defaultdict(list)
for entry in all_entries:
    norm = normalize_name(entry['name'])
    normalized_to_originals[norm].append(entry)

# Step 3: Resolve duplicates with fuzzy matching
unique_people = {}  # canonical_name -> {'field_counter': Counter, 'frequency': int}
threshold = 0.9

# Sort normalized keys for ordered processing
sorted_norms = sorted(normalized_to_originals.keys())

for norm in sorted_norms:
    originals = normalized_to_originals[norm]
    name_counter = Counter(e['name'] for e in originals)
    canonical = max(name_counter, key=name_counter.get)
    field_counter = Counter(e['field'] for e in originals)
    freq = len(originals)

    # Check against existing uniques for merge
    to_merge = None
    for existing in list(unique_people.keys()):
        similarity = difflib.SequenceMatcher(None, canonical.lower(), existing.lower()).ratio()
        if similarity >= threshold:
            to_merge = existing
            break

    if to_merge:
        unique_people[to_merge]['field_counter'] += field_counter
        unique_people[to_merge]['frequency'] += freq
    else:
        unique_people[canonical] = {
            'field_counter': field_counter,
            'frequency': freq
        }

# Step 4: Rank and refine list
people_list = []
for name in unique_people:
    entry = unique_people[name]
    most_common_field = entry['field_counter'].most_common(1)[0][0]
    freq = entry['frequency']
    people_list.append({'name': name, 'field': most_common_field, 'frequency': freq})

# Sort descending by frequency, ascending by name
sorted_people = sorted(people_list, key=lambda x: (-x['frequency'], x['name']))

# Refine to max 500
if len(sorted_people) > 500:
    sorted_people = sorted_people[:500]
# Min 300: if less, keep all

# Step 5: Write to refined CSV file
with open('geniiAggregateSortFreq.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'field', 'frequency'])
    for p in sorted_people:
        name_safe = p['name'].replace(',', '-')
        field_safe = p['field'].replace(',', '-')
        writer.writerow([name_safe, field_safe, p['frequency']])