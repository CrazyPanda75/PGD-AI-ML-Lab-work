# Build Multilayer perceptron without using lib and find total error
import numpy as np
x1=0.05 # Given input
x2=0.10 # Given input
b1=0.35 # Given bias
b2=0.60 # Given bias
d1=0.01 # Given desired output
d2=0.99 # Given desired output
w=([0.15,0.20,0.25,0.30,0.40,0.45,0.50,0.55]) # Given weights
a=([0,0,0,0]) # a is array to store weighted sum pre activation function
h=([0,0,0,0]) # h is post activation function
a[0]=(x1*w[0])+(x2*w[1])+b1
a[1]=(x1*w[2])+(x2*w[3])+b1
h[0]=1/(1 + np.exp(-a[0]))
h[1]=(1 + np.exp(-a[1]))
a[2]=(h[0]*w[4])+(h[1]*w[5])+b1
a[3]=(h[0]*w[6])+(h[1]*w[7])+b1
h[2]=(1 + np.exp(-a[2]))
h[3]=(1 + np.exp(-a[3]))
Et=(0.5*(d1-h[2])**2)+(0.5*(d2-h[3])**2) # Total error
print(Et)









