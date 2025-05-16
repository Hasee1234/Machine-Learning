# import matplotlib.pyplot as plt
# import numpy as np

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
# x=np.linspace(0,10,100)
# y1=np.sin(x)
# y2=np.cos(x)

# plt.figure(figsize=(10,6))
# plt.fill_between(x,y1,y2,color='green',alpha=0.5)
# plt.plot(x,y1,color='red',label='sin(x)')
# plt.plot(x,y2,color='blue',label='cos(x)')
# plt.title('Area Plot')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()


import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import subplot


air = pd.read_csv('air.csv')
# print(air.head())

air['station_paris'].plot()
air.plot.scatter(x='station_london',y="station_paris")
air.plot.box()
air.plot.area(figsize=(9,4), subplots=True)
plt.show()

# ---------------------------------------

plt.plot(air["station_london"], air["station_paris"], "g^")
# we can you these args for different types of plots
"""Plotting Style Codes:
- 'ro': Red circles
- 'g^': Green triangles
- 'b*': Blue stars
- 'c+': Cyan inlines
- 'ko': Black squares
- 'o': 
- 'rx': Red x's
- 'gD': Green diamonds
- 'g--': Green dashed line
- 'r--': Red dashed line
- 'bs': Blue squares
- 'k-': Black solid line
- 'm--': Magenta dashed line"""
plt.plot([1,5,15,35], [23,34,55,45],"k-")                                                     #use for line 
# plt.scatter(air["station_london"], air["station_paris"],)                                     #use to show the data as of points
# plt.hist(air["station_london"], density=True, facecolor="g" , histtype="stepfilled" )         #use to show the data in the form of histogram

# ---Hist is mostly use for the distribution of data---
# density=True:
# When set to True, the histogram will display the probability density instead of the raw counts. This means that the area under the histogram will sum to 1, which is useful for comparing distributions.
# facecolor="g":
# This specifies the color of the histogram bars. In this case, "g" stands for green. You can change this to other color codes (like "r" for red, "b" for blue, etc.) or use hex color codes (like #FF5733).
# histtype="step":
# This argument determines the type of histogram to draw. The "step" type creates a line plot that outlines the histogram instead of filling it with color. Other options include:
# "bar": Traditional filled bars.
# "step"
# "barstacked": Stacked bars.
# "stepfilled": Filled step histogram.

plt.xlabel("Station London Values")
plt.ylabel("Probability Density")
plt.suptitle("Histogram of Station London Values")
# plt.show()




# ------------------- This code creates a figure with 3 subplot.
groups = ['group 1', 'group2', 'group3']
values = [5,25,100]
# plt.figure(figsize=(9,4))
# # Creating a bar plot for the groups and their corresponding values
plt.subplot(231)
plt.bar( groups,values )
# Creating a scatter plot for the values and groups
plt.subplot(232)
plt.scatter(values, groups, color='r')
# Creating a line plot for the values and groups
plt.subplot(233)
plt.plot(values, groups, 'ro-')
plt.show()

# --------------------- other way for subplot
# plt.figure(figsize=(9,3))
# plt.subplot(1,3,1)
# plt.bar(groups, values)
# plt.subplot(1, 3, 2)
# plt.scatter (values, values)
# plt.subplot(1, 3, 3)
# plt.plot(values) 
# plt.suptitle("this is categorical")
# # plt.tight_layout(pad=2.0)
# plt.show()



#subplots this is not same from the previous both  ==> we can say that this is for the 2_D plots
# fig , axs = plt.subplots(2,3,figsize=(9.3))
# axs[0,0].bar(groups,values)
# fig, axs = plt.subplots(2, 3, figsize=(9,3))
# axs[0,0].bar(groups, values, color='purple')
# axs[0,0].set_title('Bar Chart')
# axs[0,1].hist(values)
# axs[0,1].set_title("histogram")
# axs[0,2].plot(groups, values, 'g--')
# axs[0,2].set_title("line charts")
# axs[1,0].bar(groups, values, color='yellow')
# axs[1,1].scatter(groups, values)
# axs[1,2].plot(values, groups, 'rs')
# plt.show()