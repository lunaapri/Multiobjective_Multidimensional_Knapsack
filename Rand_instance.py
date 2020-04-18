
import numpy as np
import math

def m_KP_MOP(n, m, J, U):
    #n number of items
    #m number of dimensions in knapsack
    #J number of knapsacks

    if U < 40:
        return "Error, U must be greater than 40"

    np.random.seed(77973)

    c = np.random.randint(1, high=U, size = (n, J))
    a = np.random.randint(1, high=U, size = (n, m))

    b = []

    for k in range(m):
        a_np = np.array(a)
        sum = 0
        for i in range(n):
            sum += a[i][k]
        temp = a_np[:,k]
        np.append(temp, math.ceil(0.5*sum))
        b.append(max(temp))  #b is capacity in k


    # Writing to txt
    instance_num = input("What is the instance number:   ") #for text file name
    instance = "instance" + str(instance_num)

    file = open(instance + ".txt","w+")
    file.write(str(n) +  "\n")
    for i in range(len(b)):
        file.write(str(b[i]))
        file.write('\n')

    for j in range(J):
        s = str(np.array(c)[:,j]*-1)
        s = list(s)
        s.pop(0)
        s.pop(len(s) - 1)
        s = "".join(s)
        file.write(s) #check that it's negative 1
        file.write('\n')

    for i in range(m):
        s = str(np.array(a)[:,i])
        s = list(s)
        s.pop(0)
        s.pop(len(s) - 1)
        s = "".join(s)
        file.write(s)
        file.write('\n')

    file.close()

m_KP_MOP(5, 1, 2, 40)










