#PROGRAM TO CHECK IF GIVEN IMAGE IS OF RED ROSE BY USING RBFN NODE
import numpy as np
import cv2
import math
import matplotlib.pyplot as plt
import glob
import os
import natsort
#To count number of files in training folder
count = 0
for path in os.listdir('D:\python\GIT_file\Flower_img_for_rbfn_node\Train'): #Change this dir as per train folder location
    if os.path.isfile(os.path.join('D:\python\GIT_file\Flower_img_for_rbfn_node\Train', path)): #Change this dir as per train folder location
        count += 1
i=0
j=0
k=0
phy=np.zeros((count,count))
im2matf=np.zeros((count,200,200))
nodeimg=np.zeros((count,200,200,3))
hsvnodeimg=np.zeros((count,200,200,3))
#Here we imort image form folder and save it in matrix form in nodeimg
nodeimg = [cv2.imread(file) for file in (natsort.natsorted(glob.glob('D:\python\GIT_file\Flower_img_for_rbfn_node\Train\*')))] #Change this dir as per train folder location
#Here we convert image from gbr to hsv and extract only pure red parts of image
lower_red=np.array([155,25,0])
upper_red=np.array([179,255,255])
while (i < count):
 hsvnodeimg[i]=cv2.cvtColor(nodeimg[i],cv2.COLOR_BGR2HSV)
 im2matf[i]=cv2.inRange(hsvnodeimg[i],lower_red,upper_red)
 i=i+1
#h='image' #To give title to the image we want to check
#cv2.imshow(h,im2matf[2])  #To check red componets of image
#cv2.waitKey(0)            #To hold image
j=0
i=0
k=0
#Here we Process and calculate output of RBFN node i.e. phy
for j in range(0,count):
    for k in range(0,count):
     x=im2matf[j]
     u=im2matf[k]
     diff=x-u
     sum=(diff.sum())*0.00001     #Here we multiply sum by 0.00001 to scale down the sum
     p = math.exp(-2*((sum)**2))
     phy[j][k] = p
w=np.ones((count))
wn=np.zeros((count))
wu=0
#Here we calculate weighted sum and pass it through sigmoid function (activation function) to get output y
#Then we convert y to binary form that if y>0.5 its red rose else its not red rose
while (wu<28):
 j=0
 i=0
 k=0
 wsum=np.zeros((count))
 wx=np.zeros((count,count))
 for j in range(0,count):
     for k in range(0,count):
        wx[j][k]=w[k]*phy[j][k] 
 for i in range(0,count):
    wsum[i]=(wx[i]).sum()
 j=0
 i=0
 k=0
 y=np.ones((count))
 for j in range(0,count):
    y[j]=1/(1 + math.exp(-wsum[j]))
    if y[j]>=0.5:
        print("its red rose")
    else:
        print("its not red rose")
 j=0
 i=0
 k=0
 #Here we input desired output
 d=[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0]
 et=np.ones((count))
 ew=np.zeros((count,count))
 #Here we calculate total error
 for i in range(0,count):
    et[i]=2*((d[i]-y[i])**2)
 i=0
 #Here we calculate indivisual weight error and update weights
 for j in range(0,count):
     for k in range(0,count):
        ew[j][k]=(y[k]-d[k])*(1/(1 + math.exp(-wsum[k])))*(1-(1/(1 + math.exp(-wsum[k]))))*(phy[j][k])
        wn[k]=w[k]-(0.5*ew[j][k])
        w[k]=wn[k]
 
 wu=wu+1
print ("updated weights are=",w)



#After we get updated weights we run the program to test against test images
tcount = 0
#To count number of files in training folder
for path in os.listdir('D:\python\GIT_file\Flower_img_for_rbfn_node\Test'): #Change this dir as per test folder location
    if os.path.isfile(os.path.join('D:\python\GIT_file\Flower_img_for_rbfn_node\Test', path)): #Change this dir as per test folder location
        tcount += 1
tim2matf=np.zeros((tcount,200,200))
tnodeimg=np.zeros((tcount,200,200,3))
thsvnodeimg=np.zeros((tcount,200,200,3))
#Here we imort image form test folder and save it in matrix form in tnodeimg
tnodeimg = [cv2.imread(tfile) for tfile in (natsort.natsorted(glob.glob('D:\python\GIT_file\Flower_img_for_rbfn_node\Test\*')))] #Change this dir as per test folder location
i=0
#Here we convert image from gbr to hsv and extract only pure red parts of test image
while (i < tcount):
 thsvnodeimg[i]=cv2.cvtColor(tnodeimg[i],cv2.COLOR_BGR2HSV)
 tim2matf[i]=cv2.inRange(thsvnodeimg[i],lower_red,upper_red)
 i=i+1
#cv2.imshow(h,tim2matf[2])
#cv2.waitKey(0)
j=0
i=0
k=0
#Here we Process and calculate output of RBFN node for test images i.e. phy
for j in range(0, tcount):
    for k in range(0, count):
     x=tim2matf[j]
     u=im2matf[k]
     diff=x-u
     sum=(diff.sum())*0.00001
     p = math.exp(-2*((sum)**2))
     phy[j][k] = p
j=0
k=0
i=0
#Here we calculate weighted sum and pass it through sigmoid function (activation function) to get output y
#Then we convert y to binary form that if y>0.5 Test is red rose else Test is not red rose
wsum=np.zeros((count))
wx=np.zeros((tcount,count))
for j in range(0, tcount):
    for k in range(0, count):
        wx[j][k]=w[k]*phy[j][k] 
for i in range(0, tcount):
    wsum[i]=(wx[i]).sum()
j=0
i=0
k=0
y=np.ones([tcount])
for j in range(0, tcount):
    y[j]=1/(1 + math.exp(-wsum[j]))
    l='lul'
    if y[j]>=0.5:
        test=j+1
        cv2.imshow(l,tnodeimg[j])
        print("Test",test,"is red rose")
        cv2.waitKey(0)
    else:
        test=j+1
        cv2.imshow(l,tnodeimg[j])
        print("Test",test,"is not red rose")
        cv2.waitKey(0)
    j=j-1