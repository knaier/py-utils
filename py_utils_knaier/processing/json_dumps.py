import json

numbers = [1,2,3,4,5,6]

with open('../../resources/dumps.json', 'w') as f:
    json.dump(numbers, f)

print(json.dumps({"field": "test"}))

print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':')))

# pretty print
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))

deserialized = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print(deserialized[1]['bar'])

# Use the json.tool on the terminal to validate json
# echo '{"json":"obj"}' | python -m json.tool
# echo '{1.2:3.4}' | python -m json.tool
