
print(__package__)

# Read a file into a variable
# Using 'with' the open, means the open file will be closed at end of this block automatically, like Closable 
with open('../../resources/digits.txt') as file_object:
    # this reads the whole file
    contents = file_object.read()

print(contents)

print("What about reading line by line?")
with open('../../resources/digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())  # removes the training new line so there isnt a double print line

print("What about reading into a list of lines?")
with open('../../resources/digits.txt') as file_object:
    lines = file_object.readlines()

print(f"We have read {len(lines)} of text the first line 5 chars is {lines[0][:5]}")

# Note when writing, you need the 'w' mode to indicate its in write mode
# 'a' is append mode
with open('../../resources/digits_new.txt', 'w') as file_object:
    file_object.write("i love programming")
