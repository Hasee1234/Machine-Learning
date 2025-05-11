# task 1
import numpy as np
array = np.arange(10,21)
# print(array[:3])
array[10]=100
# print(array)


# task 2
array2=np.array([1,2,3,4,5,6,7,8,9,10])
even=array2[1:10:2]
# print(even)
even[3]=100
# print(even)#yes it does change

# task3

array3=np.array([[[1,2,3],
                 [4,5,6],
                 [7,8,9]]])
# print(array3)
array3[0,1,2]=100
# print(array3)#yes it will change

second_column=array3[0, :, 1]
# print(second_column)
 
#task4
array4 = np.arange(1, 9)
array5=array4.reshape(4,2)
# print(array5)

#task5
array6=np.zeros(5)
print(array6)

array7=np.ones([3,3])
print(array7.shape)

array8=np.linspace(0,100,11)
print(array8)

# task6
arr=np.array([8,2,5,1,7])
print(np.sort(arr))

a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.concatenate((a,b)))

# task7
array9=np.arange(1,7)
print(array9.ndim)
print(array9.shape)
print(array9.reshape(2,3))

array10=np.arange(1,13)
print(array10[:,np.newaxis])

array11=np.arange(1,13)
array11=array11.reshape(3,4)
print(np.expand_dims(array11,axis=0))
