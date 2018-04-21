
import scipy.stats as st;
import numpy as np;
import matplotlib.pyplot as plt
from scipy.stats import norm

# Normal Distribution
def calculate_normal_ppf (value) :
	return st.norm.ppf(value);

def calculate_normal_cdf (value) :
	return st.norm.cdf(value)

def draw_z_score(x, cond, mu, sigma, title):
    y = norm.pdf(x, mu, sigma)
    z = x[cond]
    plt.plot(x, y)
    plt.fill_between(z, 0, norm.pdf(z, mu, sigma))
    plt.title(title)
    plt.show()

def getZlessthan(z_value):
	x = np.arange(-3,3,0.001)
	z0 = calculate_normal_cdf(z_value)
	draw_z_score(x, (x < z_value), 0, 1, f"z<{z_value}")
	print("Z0:",z0);

def getZgreatherThan(z_value):
	x = np.arange(-3,3,0.001)
	draw_z_score(x, (x > z_value), 0, 1, f"z>{z_value}")
	z0 = calculate_normal_cdf(z_value)
	print("Z0:",z0);

def getZInRange(z_init,z_final):
	x = np.arange(-3,3,0.001)
	draw_z_score(x, (z_init < x) & (x < z_final), 0,1, f"{z_init}<z<{z_final}");
	z_greatherInit = calculate_normal_cdf(z_init)
	z_lessFinal = calculate_normal_cdf(z_final);
	print("Result:",z_lessFinal-z_greatherInit);



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
