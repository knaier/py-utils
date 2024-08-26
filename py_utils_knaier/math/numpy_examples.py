import numpy as np
import sys

# https://numpy.org/doc/stable/user/quickstart.html

# Force full print for np
np.set_printoptions(threshold=sys.maxsize)  # sys module should be imported

# Sum Product / Dot Product
print(np.dot([1,2,3], 2)) # [2, 4, 6]
print(np.dot([1,2,3], [2,4,8])) # 34

# norm = distance from origin / hypotenuse - https://en.wikipedia.org/wiki/Norm_(mathematics)
print(np.linalg.norm([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]))

# create array
print("Create array")
a = np.array([2, 3, 4])
print(f"int is {a.dtype}={a}")
b = np.array([1.2, 3.5, 5.1])
print(f"float is {b.dtype}={b}")

c = np.array([(1.5, 2, 3), (4, 5, 6)])
print(f"2d array {b.dtype}={c}")

print(f"Zeros is {np.zeros((3, 4))}")
print(f"Ones [2][3]=len(4) is {np.ones((2, 3, 4), dtype=np.int16)}")
print(f"Empty is {np.empty((2, 3))}")

# create array via arange, similar to range but returns an array
print(f"arange(10,30,5)={np.arange(10, 30, 5)}")
print(f"arange(0,2,0.3)={np.arange(0, 2, 0.3)}")
print(f"arange(5)={np.arange(5)}")
print(f"arange(12).reshape(4,3)={np.arange(12).reshape(4, 3)}")

# arange with floating point doesnt give a predictible number of results, so better to use linspace
print(f"linspace(0,2,9) i.e. 9 numbers between 0 and 2={np.linspace(0, 2, 9)}")
x = np.linspace(0, 2 * np.pi, 10)        # useful to evaluate function at lots of points
print(f"linspace(0,2*pi,10) i.e. 100 numbers between 0 and 2*pi={x}")

print()
print("Trig funcs")
f = np.sin(x)
print(f"sin(linspace results from pi)={f}")

# Arithmetic
print()
print("Basic Arithmetic")
A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
print(f"a={A}, b={B}")
print(f"elementwise product a * b={A * B}")
print(f"matrix product a @ b={A @ B}")
A.dot(B)  # another matrix product
print(f"matrix product via dot a.dot(b)={A.dot(B)}")
