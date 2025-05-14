import numpy as np
# b=np.zeros(2)
# b=np.zeros([2,3])
# b=np.zeros([2,2,3])
# b=np.zeros([2,2,2,3])
# b=np.zeros([2,2,2,3],dtype=np.int64)#to convert into float
# print(b)

c=np.ones([2,2,2,3])
# print(c)

d=np.empty([2,2,2,3])#it will create differet memory locations so create different numbers
# print(d)

e=np.arange(20)#create array of 15 elements
# print(e)

f=np.linspace(2,15,60)#to tell about jumps
# print(f)

# how to sort arrays

# print(np.sort(d))#default quick sort
# print(np.sort(d),kind='mergesort')#can use any sort by using kind parameter
# print(np.argsort(d))#it will tell index


# task
shape = (2, 3, 4, 5)
array = np.empty(shape, dtype=int)
value = 1
for i in range(shape[0]):
    for j in range(shape[1]):
        for k in range(shape[2]):
            for l in range(shape[3]):
                array[i, j, k, l] = value*2-1#for odd
                value += 1
# print(array)
# print(np.concatenate((b,c)))
# print(np.concatenate((b,c),axis=1))