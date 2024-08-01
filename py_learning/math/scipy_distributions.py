import scipy
import math

print("Normal Standard Distribution (Mean=0, StdDev=1)")
standard_normal_distribution = scipy.stats.norm(0,1)
for i in range(-2,3):
    print(f"i={i}={standard_normal_distribution.pdf(i)}")

print("Cumulative Standard Distribution (Mean=0, StdDev=1)")
for i in range(-2,3):
    print(f"i={i}={standard_normal_distribution.cdf(i)}")

print("Normal Standard Distribution - Implemented (Mean=0, StdDev=1)")
def normpdf(x, mean, sd):
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

for i in range(-2,3):
    print(f"i={i}={normpdf(i, 0, 1)}")

print("Normal Standard Distribution - Implemented (Mean=0, StdDev=1)")
scipy.stats.norm(loc=100, scale=12)
#where loc is the mean and scale is the std dev
print(f"Find a random value from the distribution: {scipy.stats.norm.rvs(loc=100, scale=12)}")

#To find the probability that the variable has a value LESS than or equal
#let's say 113, you'd use CDF cumulative Density Function
print(f"Find The CDF gives a probability a variable has a value less than or equal to something i.e. 113=: {scipy.stats.norm.cdf(113,100,12)}")
print(f"Find The SF=survival function probability of a variable has a value greater than or equal to i.e. 125=: {scipy.stats.norm.sf(125,100,12)}")

#To find the variate for which the probability is given, let's say the
#value which needed to provide a 98% probability, you'd use the
#PPF Percent Point Function
print(f"Find Using The PPF=Percent Point Function for the variate for which the probability is given, i.e. the value for a probability i.e. 98%=: {scipy.stats.norm.ppf(.98,100,12)}")
