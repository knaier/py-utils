name = "evelina smith"

print(f'Title Case: {name.title()}')
print(f'Upper Case: {name.upper()}')
print(f'Lower Case: {name.lower()}')
print("-------------")

daughter = f"I love {name.title()}"
print(daughter)
print("-------------")

oldPython3point5AndBeforeEquivalent = "Pre Python 3.6 fSting didnt exist, so have to use .format() i.e. I love {} {}".format(name.title(), name.upper())
print(oldPython3point5AndBeforeEquivalent)
print("-------------")

strip = " text "
print(f"Length of '{strip}' is {len(strip)}")
print(f"str.rstrip() Length of '{strip.rstrip()}' is {len(strip.rstrip())}")
print(f"str.lstrip() Length of '{strip.lstrip()}' is {len(strip.lstrip())}")
print(f"str.strip() Length of '{strip.strip()}' is {len(strip.strip())}")
print("-------------")

strip = 'single quotes with a extra \' inside need to be escaped'
print(strip)
print("-------------")

print("A set of words".split())
print("-------------")
