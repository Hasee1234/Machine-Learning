import numpy as np
import matplotlib.pyplot as plt

# x=np.linspace(0,10,100)
# y=np.cos(x)
# plt.figure(figsize=(10,6))
# plt.plot(y,label='cosine wave',color='green')
# plt.title("cosine wave")
# plt.show()

# x=np.random.rand(100)
# y=np.random.rand(100)
# colors=np.random.rand(100)
# sizes=1000*np.random.rand(100)
# plt.scatter(x,y,c=colors,s=sizes,marker='^')
# plt.show()

# categories = ['X', 'Y', 'Z']
# values = [5, 15, 10]
# plt.figure(figsize=(10,6))
# plt.bar(categories,values,color='blue')
# plt.xlabel("categories")
# plt.ylabel("values")
# plt.title("bar plot")
# plt.show()

# x=np.random.normal(0,10,1000)
# plt.figure(figsize=(10,6))
# plt.hist(x,bins=25,alpha=0.6,edgecolor='black')
# plt.title("normal distribution")
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()

# labels = ['P', 'Q', 'R']
# sizes = [40, 30, 30]
# plt.pie(sizes,labels=labels,autopct='%0.1f%%')
# plt.axis('equal')
# plt.legend()
# plt.show()

# x=np.linspace(0,10,100)
# fig,axes=plt.subplots(2,2)

# axes[0,0].plot(x,np.sin(x))
# axes[0,0].set_title('sin x')
# axes[0,1].plot(x,np.sin(x))
# axes[0,1].set_title('sin x')
# axes[1,0].plot(x,np.sin(x))
# axes[1,0].set_title('sin x')
# axes[1,1].plot(x,np.sin(x))
# axes[1,1].set_title('sin x')
# plt.tight_layout()
# plt.show()

# x = np.arange(5)
# y = [1, 3, 2, 4, 5]
# error = [0.2, 0.1, 0.3, 0.2, 0.1]
# plt.errorbar(x,y,xerr=error,fmt='^',color='red')
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# categories = ['A', 'B', 'C']
# group1 = [5, 10, 15]
# group2 = [10, 5, 10]

# plt.bar(categories,group1)
# plt.bar(categories,group2,bottom=group1)
# plt.xlabel("X")
# plt.ylabel("Y")
# # plt.legend()
# plt.show()

# x=np.linspace(0,10,100)
# y1=np.sin(x)
# y2=np.cos(x)
# plt.fill_between(x,y1,y2,color='green')
# plt.plot(x,y1,color='red')
# plt.plot(x,y2,color='blue')
# plt.show()

x=np.random.rand(100)
z=np.random.rand(100)
color=np.random.rand(100)
sizes=1000*np.random.rand(100)

y=np.random.normal(0,1,1000)

fig,axes=plt.subplots(1,2,figsize=(12,6))
axes[0].scatter(x,z,c=color,s=sizes)
axes[0].set_title("scatter plot")

axes[1].hist(y,bins=30)
axes[1].set_title("histogram")
plt.show()
