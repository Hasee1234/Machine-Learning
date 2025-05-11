import numpy as np
b=np.array([[1,2,3],[5,6,9]])
c=np.array([[1,2,3],[5,6,9]])
x=np.array([[1,2,3],[5,6,9]])
# print(np.concatenate((b,c)))


# Creating a 4D array 
a = np.array([[[[1, 2,3], [3,5, 4]], 
               [[5, 6,6], [7, 8,6]]],
              [[[9, 6,10], [11,5, 12]], 
               [[13,6, 14], [15, 6,16]]]])

# print(a)
# print(a.ndim)
# print("Shape of the array:", a.shape)
# print(a.reshape(3,2,4))
# print(a.reshape(12,2))#for 2dimensional conversion
# print(a.reshape(2,12))
# print(a.reshape(2,2,2,3,1))#for 5dimensional conversion

z=np.array([[1,2,3],[5,6,9],[2,4,5]])#tricky to reshape odd arrays

j=np.array([2,2,3,6,9,5,6,8,])
print(j.ndim)
print(j.shape)
print(j[np.newaxis,:].shape)
print(j[:,np.newaxis].shape)
print(np.expand_dims(j,axis=0).shape)#another method to increase dimentionality