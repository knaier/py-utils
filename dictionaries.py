alien_o = {
    'colour': 'green', 
    'points': 5,
    # 'ships': ['powerful'],
    # 'attrs': {'weapon': None}
    }

print(f"alien colour is {alien_o['colour']}")

# Note since Python 3.7, dictionaries maintain their order
print(alien_o)

# if you sort, you only get the keys sorted
sortedKeys = sorted(alien_o, reverse=True)
print(sortedKeys)

# new field and then delete
alien_o['new_field'] = 'garbage'
print(alien_o)
del alien_o['new_field']
print(alien_o)

# use get to retrieve if the value may not be there to avoid errors
invalidField = alien_o.get("field_doest_exist")
print(f"invalid field is {invalidField}, is None={invalidField == None}")

# loop through
for key, value in alien_o.items():
    print(f"{key}={value}")

print(f"keys={alien_o.keys()}")

# Sets print the same as dictionaries i.e. {green, 5}, but dont show a value. If there is braces and no key=value, its a set
alienValuesAsSet = set(alien_o.values())
print(alienValuesAsSet)