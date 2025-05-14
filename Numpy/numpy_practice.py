import numpy as np
# a=np.array([1,2,3,4,5])
# a=np.array([[[1,2,3],
#             [4,5,6],[7,8,9]]])
# print(a.shape)
# print(a.ndim)
# print(a[0,2,2])
# array=np.array([[[[[1,2,3],[4,5,6]]]]])
# print(array.shape)
# print(array.ndim)
# print(array[0,0,0,1,1])

# b=np.array([[[[1],[10]]]])
# print(b.ndim)
# print(b[0,0,1,0])

# c=np.array([[[[[1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [10,11,12],
#     [13,14,15]]]]])
# print(c.ndim)

zeros=np.zeros([2,],dtype=np.int64)
zeros2=zeros.astype(int)
print(zeros2)
print(zeros.shape)
print(zeros.ndim)

ones=np.ones([5,5,6,7,7],dtype=np.int64)
print(ones)
print(ones.shape)
print(ones.ndim)

# empty=np.empty([1,2,3],dtype=np.int64)
# print(empty)

# arrange=np.arange(2,11,2)#use to specify gap
# print(arrange)

# linspace=np.linspace(0,1,100)#use to specify intervals bw two numbers
# print(linspace)

# arr=np.array([1,6,8,3,0,3,7,4])
# sort=np.sort(arr,kind='quicksort')
# print(sort)
# arg=np.argsort(arr)
# print(arg)

# arr_4d=np.empty([4,4,4,4,])
# for i in range(4):
#     for j in range(4):
#         for k in range(4):
#             for l in range(4):
#                 arr_4d[i,j,k,l]=1
                # print(arr_4d)
                
#identity
# arr_identity=np.identity(3)
# print(arr_identity)
# arr_identity=np.eye(3)
# print(arr_identity)

# concatenation 
x=np.array([[1,2,3,4],[5,6,7,8]])
# y=np.array([[1,2,3,4],[5,6,7,8]])
# d=np.concatenate((x,y))
# print(d)
# print(x.size)
# print(x.reshape(4,2))

#new axis
# newaxis=x[np.newaxis,:,:]
# print(newaxis.shape)
# print(newaxis.size)
# print(newaxis.ndim)

# expand array 
expand_x=np.expand_dims(x, axis=1)
# print(expand_x)
# print(expand_x.shape)
# print(expand_x.ndim)