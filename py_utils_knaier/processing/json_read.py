import json

with open('../../resources/sample.json', 'r') as f:
    all_data = json.load(f)

print(all_data)

for row in all_data:
    print(row['sample'])
