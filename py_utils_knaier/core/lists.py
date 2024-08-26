bicycles = ['trek', 'cannondale', 'unknown']

# Access via index
print(f"First elem is {bicycles[0]}")
print(f"Last item is {bicycles[-1]}")
print(f"Second to Last item is {bicycles[-2]}")
print("-------------")

# Change value
bicycles[2] = "honda"
print(f"Last item is {bicycles[-1]}")
print("-------------")

# Append at end .append()
bicycles.append("Apollo".lower())
print(f"Last item is {bicycles[-1]}")
print("-------------")

# Insert at position, .insert()
bicycles.insert(0, "hybrid")
print(bicycles)
print("-------------")

# Remove from a list using del keyword
del bicycles[0]
print(bicycles)
print("-------------")

# Remove a item by value, using .remove()
bicycles.remove('honda')
print(bicycles)
print("-------------")

# Pop off (and remove) the top of the stack / last item in the list
lastItem = bicycles.pop()
print(f"last item removed was {lastItem} leaving {bicycles}")
print("-------------")

# Sorting
bicycles.sort()
print(f"sorted bicycles {bicycles}")
bicycles.sort(reverse=True)
print(f"sorted bicycles in reverse {bicycles}")
print("-------------")

# Sorting Temporarily
print(f"sorted bicycles temporarily {sorted(bicycles)}")
print("-------------")

# Reverse order i.e. reverse of what the list was ordered as
bicycles.reverse()
print(f"reversed {bicycles}")
print("-------------")

# Utils
print(f"Length of a list {len(bicycles)}")
print("-------------")

# List from range
values = list(range(5))
print(values)
print("-------------")
