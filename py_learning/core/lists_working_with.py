magicians = ["alice", 'david', "carolina"]

# for 
for magician in magicians:
    print(magician)

print(f"Finished looping over {len(magicians)} magicians")
print(f"Last value of magician={magician}")
print("-------------")

# for numerical range, will print 0-4
for value in range(0,5):
    print(value)
print("-------------")

# Utils
print(f"max()={max(range(5))}, min()={min(range(5))}, sum()={sum(range(5))}")
print("-------------")

# List Comprehension
squares = [value**2 for value in range(1,10)]
print(squares)
print("-------------")

# Slicing the list
print(f"squares[0:3]={squares[0:3]}")
print(f"starts at 0 automatically - squares[:3]={squares[:3]}")
print(f"rest of items starting at - squares[3:]={squares[3:]}")
print(f"last n items - squares[-2:]={squares[-2:]}")
print("-------------")

# Copy a list
squares_copy = squares[:]
print(squares_copy)
