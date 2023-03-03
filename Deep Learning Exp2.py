# Implement perceptron and find updated weights after all iterations
# given: starting weights = [0,0,-1,2]
# 4 feature input =([1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1])
# Desired output = (0,1,1,1,1,1,1,1)
# Learning rate = 1
import numpy as np
w=np.array([0,0,-1,2])     # given starting weight
input=([1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1])  # 4 feature inputs in array form
y=(0,1,1,1,1,1,1,1)  # given expected output
n=1 # learning rate
j=0
while j<4:
 i=0
 while i<8:
  weighted_sum=sum(input[i]*w)  # weighted sum
  print("weighted_sum =",weighted_sum)
  if weighted_sum>=0: # threshold function
   h=1        
  else:
   h=0        
  print("actual output of neuron is = ",h)       # h= real output
  w[0]= w[0]+((y[i]-h)*n*(input[i][0]))   # weight 1 = weight 1 + change in weight 1
  w[1]= w[1]+((y[i]-h)*n*(input[i][1]))   # weight 2 = weight 2 + change in weight 2
  w[2]= w[2]+((y[i]-h)*n*(input[i][2]))   # weight 3 = weight 3 + change in weight 3
  w[3]= w[3]+((y[i]-h)*n*(input[i][3]))   # weight 4 = weight 4 + change in weight 4
  print(w)    # updated weight
  i=i+1
 j=j+1
print("Final updated weight after all iterations are = ",w)