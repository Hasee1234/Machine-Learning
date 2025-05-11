import matplotlib.pyplot as plt
import numpy as np

#sin Wave
# x=np.linspace(0,10,100)
# y=np.sin(x)

# plt.plot(x,y,label='Sine Wave',color='green',linestyle='dashed')
# plt.title('sine wave')
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.legend()
# plt.grid(True)
# plt.show()

#scatter plots
# x=np.random.rand(100)
# y=np.random.rand(100)
# colors=np.random.rand(100)
# sizes=1000*np.random.rand(100)
# plt.figure(figsize=(10,6))
# plt.scatter(x,y,c=colors,s=sizes,alpha=1,marker='^')
# plt.title("scatter plot")
# plt.xlabel('x')
# plt.ylabel('y')
# plt.colorbar()
# plt.show()

#barplot
# categories=['A','B','C','D',]
# Values=[10,15,5,25]

# plt.figure(figsize=(10,6))
# plt.bar(categories,Values,color="green",alpha=1)
# plt.title("Bar Plot")
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.show()

#histogram
# data=np.random.normal(0,1,1000)

# plt.figure(figsize=(10,6))
# plt.hist(data,bins=30,color="green",alpha=0.7,edgecolor="black")
# plt.title('Histogram')
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.show()

#pie chart
# sizes=[30,40,10,15,5]
# labels=['A','B','C','D','E']

# plt.figure(figsize=(10,6))
# plt.pie(sizes,labels=labels,autopct='%0.1f%%')
# plt.title("pie chart")
# plt.axis('equal')
# plt.show()

# subplots
# x = np.linspace(0, 10, 100)
    
# fig,axes = plt.subplots(2, 2)
    
#     # Plot 1
# axes[0, 0].plot(x, np.sin(x))
# axes[0, 0].set_title('Sine')
    
#     # Plot 2
# axes[0, 1].plot(x, np.cos(x))
# axes[0, 1].set_title('Cosine')
    
#     # Plot 3
# axes[1, 0].plot(x, np.tan(x))
# axes[1, 0].set_title('Tangent')
    
#     # Plot 4
# axes[1, 1].plot(x, np.exp(x))
# axes[1, 1].set_title('Exponential')
    
# plt.tight_layout()
# plt.show()

#error bars
# x=np.arange(5)
# y=np.array([1,2,3,4,5])
# error=np.array([0.1,0.2,0.3,0.4,0.5])

# plt.figure(figsize=(10,6))
# plt.errorbar(x,y,yerr=error,fmt='^',color='green')
# plt.title('Error Bar Plot')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()

#stacked bar
# categories=['A','B','C','D']
# values1 = [10, 20, 15, 25]
# values2 = [15, 10, 20, 15]

# plt.figure(figsize=(10, 6))
# plt.bar(categories,values1,label='group 1')
# plt.bar(categories,values2,bottom=values1,label="group 2")
# plt.title('Stacked Bar Plot')
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.legend()
# plt.show()

# area plot
x=np.linspace(0,10,100)
y1=np.sin(x)
y2=np.cos(x)

plt.figure(figsize=(10,6))
plt.fill_between(x,y1,y2,color='green',alpha=0.5)
plt.plot(x,y1,color='red',label='sin(x)')
plt.plot(x,y2,color='blue',label='cos(x)')
plt.title('Area Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
