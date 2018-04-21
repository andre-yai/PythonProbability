import scipy.stats as st;
import numpy as np;
import matplotlib.pyplot as plt
from scipy.stats import norm

#Poisson
def calculatePoisson(k,mu):
	result = st.distributions.poisson.pmf(k,mu)
	return result*100;

def calculatePoissonInRange(k,mu,classification="less"):
	result = 0;
	for k_int in range(k):
		print(k_int);
		result += calculatePoisson(k_int,mu);
	if(classification == "less"):
		return result;
	if(classification == "bigger"):
		return 100 - result;



#in class
print(calculatePoisson(1000,6000));


print("Exercise Poisson:");

print("Exercise 10\n");
#homework
print("Exercise 12\n")
print(calculatePoisson(4,5.8))
print(calculatePoissonInRange(3,5.8,"bigger"));
print(calculatePoissonInRange(9,5.8));

print("\n Exercise 13 \n")
print(calculatePoisson(10,8))
print(calculatePoissonInRange(11,8,"bigger"));
print(calculatePoissonInRange(10,8));
print(calculatePoissonInRange(16,8,"bigger"));


# in class
print(getZInRange(-2.5,1.25))
# print("\n Exercise 14 \n")

# # less than
# x = np.arange(-3,3,0.001)
# print("a:")
# getZlessthan(1.04);
# #draw_z_score(x, x<z0, 0, 1.04, 'z<1.04')

# print("b:")
# getZgreatherThan(-1.64);
# #in between

# getZgrea
