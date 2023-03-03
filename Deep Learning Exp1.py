#Implement AND,OR,NOT gate using MC neuron

while(True):
    gate = input("Gate :")
    x1= int(input("Enter x1"))
    x2= int(input("Enter x2"))
    if gate == "OR":
        w1 = 2 
        w2  = 2
        b  = -1
    elif gate == "AND":
        w1 = 1 
        w2  = 1
        b  = -1
    elif gate == "NOT":
        w1 = -1
        w2 = 0
        b =  1  
    a = (x1 * w1) + (x2 * w2) + b
    if a <= 0 :
        a = 0
    else:
        a = 1

    print(a)

    if input("Do you want to exit") == "Y":
        break