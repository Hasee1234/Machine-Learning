# import seaborn as sns
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd

#box plot
# data=pd.DataFrame({
#     'Category':['A']*50+['B']*50,
#     'Value':np.random.normal(0,1,100)
# })
# plt.figure(figsize=(10, 6))
# sns.boxplot(data=data,x='Category',y='Value')
# plt.title('Box Plot')
# plt.xlabel('Category')
# plt.ylabel('Value')
# plt.show()

#violinplot
# data=pd.DataFrame({
#     'Category':['A']*50+['B']*50,
#     'Value':np.random.normal(0,1,100)
# })
# plt.figure(figsize=(10, 6))
# sns.violinplot(data=data,x='Category',y='Value')
# plt.title('Box Plot')
# plt.xlabel('Category')
# plt.ylabel('Value')
# plt.show()

#histogram with seaborn
# data=pd.DataFrame({
#     'Value':np.random.normal(0,1,1000)
# })
# plt.figure(figsize=(10, 6))
# sns.histplot(data=data,bins=30,x='Value',kde=True, color='purple', alpha=0.5)
# plt.title('Histogram with KDE')
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.show()
# plt.show()

#kde plot
# data=({
#     'category':['A']*500 +['B']*500,
#     'Value':np.concatenate([np.random.normal(0,1,500),
#                             np.random.normal(1,1,500)])
# })
# plt.figure(figsize=(10,6))
# sns.kdeplot(data=data,x='Value',hue='category')
# plt.title('Kernel Density Estimation')
# plt.xlabel('Value')
# plt.ylabel('Density')
# plt.show()

#bar plot
# data=pd.DataFrame({
#     'categories':['A','B','C','D'],
#     'value':[15,20,5,25]
# })
# plt.figure(figsize=(10,6))
# sns.barplot(data=data,x='categories',y='value',color='purple',alpha=0.8)
# plt.title('bar plot')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()

#count plot
# data=pd.DataFrame({
#     'category':np.random.choice(['A','B','C','D'],100)#100 divided in to 4( A,B,C,D)
# })
# plt.figure(figsize=(10, 6))

# sns.countplot(data=data,x='category')
# plt.title('Count Plot')
# plt.xlabel('Category')
# plt.ylabel('Count')
# plt.show()

#Heat plot
# data=pd.DataFrame(np.random.randn(10,10))
# corr=data.corr()

# plt.figure(figsize=(10, 6))
# sns.heatmap(corr,annot=True)
# plt.title('Correlation Heatmap')
# plt.show()


#pairplot
# iris=sns.load_dataset('iris')
# # plt.figure(figsize=(10,6))
# sns.pairplot(iris,hue='species')
# plt.title('Pairplot of Iris Dataset')

# plt.show()

#jointplot
# iris=sns.load_dataset('iris')
# sns.jointplot(data=iris,x='sepal_length',y='sepal_width',kind='kde')
# plt.title('Jointplot of Sepal Length and Width')
# plt.show()


#regression plot
# data=pd.DataFrame({
#     'x':np.random.rand(100),
#     'y':np.random.rand(100) * 2 + 1,
# })
# plt.figure(figsize=(10, 6))

# sns.regplot(data=data,x='x',y='y')
# plt.title('Regression Plot')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()

# data=pd.DataFrame({
#     'Category':['A']*50 + ['B']*50,
#     'value':np.random.normal(0,1,100)
# })
# plt.figure(figsize=(10, 6))
# sns.swarmplot(data=data,x='Category',y='value')
# plt.title('Swarm Plot')
# plt.xlabel('Category')
# plt.ylabel('Value')
# plt.show()



# import pandas as pd 
# import seaborn as sns  # For statistical data visualization
# import matplotlib.pyplot as plt  # For creating static visualizations
# import numpy as np  # For numerical operations

# # Load example datasets
# iris = sns.load_dataset("iris").select_dtypes(include='number') # Famous iris flower dataset
# mpg = sns.load_dataset('mpg')    # Car fuel consumption dataset
# tips = sns.load_dataset('tips')  # Restaurant tips dataset

# # 1. Heatmap Example
# # Heatmaps are useful for visualizing matrix-like data
# data = np.random.rand(5, 5)  # Create random 5x5 matrix
# sns.heatmap(data, 
#     annot=True,  # Show numbers in each cell
#     cmap='coolwarm'  # Color scheme: other options include 'viridis', 'plasma', 'magma', 'YlOrRd'
# )
# plt.title("Heatmap Example")
# plt.show()

# # 2. Boxplot Example
# # Boxplots show the distribution of data based on five number summary
# sns.boxplot(
#     x='day',  # Categorical variable for x-axis
#     y='total_bill',  # Numerical variable for y-axis
#     data=tips,  # DataFrame containing the data
#     # palette='Set3'  # Optional: color palette for different categories
# )
# plt.title("Boxplot of Total Bill Amounts by Day")
# plt.xlabel("Day of the Week")
# plt.ylabel("Total Bill ($)")
# plt.show()

# # 3. Pairplot Example
# # Pairplots show relationships between multiple variables
# sns.pairplot(
#     iris,  # DataFrame to plot
#     hue='species',  # Color points by this categorical variable
#     # palette='husl',  # Optional: color scheme
#     # diag_kind='kde'  # Optional: 'kde' for density, 'hist' for histogram
# )
# plt.suptitle("Pairplot Example", y=1.02)
# plt.show()

# # 4. Distribution Plot Example
# # Histograms with KDE show the distribution of a single variable
# sns.histplot(
#     tips['total_bill'],  # Data to plot
#     kde=True,  # Show density curve
#     # bins=30,  # Optional: number of bins
#     # color='skyblue'  # Optional: color of the histogram
# )
# plt.title("Distribution Plot with KDE")
# plt.show()

# # 5. Correlation Heatmap Example
# # Shows relationships between numeric variables
# numeric_tips = tips.select_dtypes(include='number')  # Select only numeric columns
# corr = numeric_tips.corr()  # Calculate correlation matrix
# sns.heatmap(
#     corr,  # Correlation matrix
#     annot=True,  # Show correlation values
#     cmap='viridis',  # Color scheme
#     # vmin=-1, vmax=1  # Optional: set color scale limits
# )
# plt.title("Correlation Heatmap of Numeric Variables")
# plt.show()

# # 6. Plot Aesthetics and Customization
# # Set the visual style of the plots
# sns.set_style('dark')  # Style options: 'darkgrid', 'whitegrid', 'dark', 'white', 'ticks'
# sns.set_palette('bright')  # Color palette options: 'deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind'
# sns.boxplot(x='day', y='total_bill', data=tips)
# plt.title("Customized Boxplot")
# plt.show()

# # 7. Context Adjustment
# # Adjust the scale of plot elements
# sns.set_context('notebook')  # Context options: 'paper', 'notebook', 'talk', 'poster'
# sns.scatterplot(
#     x='total_bill',  # X-axis variable
#     y='tip',  # Y-axis variable
#     data=tips,  # DataFrame
#     # hue='day',  # Optional: color points by this variable
#     # size='size',  # Optional: vary point size by this variable
#     # alpha=0.5  # Optional: transparency (0 to 1)
# )
# plt.title("Scatterplot with Notebook Context")
# plt.show()

# # 8. Violin Plot Example
# # Violin plots show the distribution of data
# sns.violinplot(
#     x='day',  # Categorical variable
#     y='total_bill',  # Numerical variable
#     data=tips,  # DataFrame
#     palette='pastel',  # Color scheme
#     # inner='box'  # Optional: 'box', 'quartile', 'point', 'stick'
# )
# plt.title('Violin Plot of Total Bill by Day')
# plt.xlabel('Day of the Week')
# plt.ylabel('Total Bill ($)')
# plt.show()

# # 9. Swarm Plot Example
# # Swarm plots show individual data points
# sns.swarmplot(
#     x='day',  # Categorical variable
#     y='total_bill',  # Numerical variable
#     data=tips,  # DataFrame
#     palette='muted',  # Color scheme
#     # size=8,  # Optional: size of points
#     # alpha=0.7  # Optional: transparency
# )
# plt.title('Swarm Plot of Total Bill by Day')
# plt.xlabel('Day of the Week')
# plt.ylabel('Total Bill ($)')
# plt.show()


