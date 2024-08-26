from statistics import NormalDist

"""
Note: statistics is available in Python >= 3.8
"""

print("Normal Standard Distribution (Mean=0, StdDev=1)")
standard_normal_distribution = NormalDist(mu=0, sigma=1)
for i in range(-2,3):
    print(f"i={i}={standard_normal_distribution.pdf(i)}")


