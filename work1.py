
#Data Loading
import pandas as pd

a=pd.read_csv("ccdata.csv")

print(a)

#Data preprocesing
v=a.isna().sum()
print(v)

#line plot
#Data plotting
# Add the essential library matplotlib
import matplotlib.pyplot as plt
import numpy as np
# create the data
a = np.linspace(0, 10)
# Draw the plot
plt.plot(a)
# Display the chart
plt.show()

#accessories using in chart
# Add the required libraries
import matplotlib.pyplot as plt
# Create the data
x = [2,4,6,8,10,12]
y = [11,22,33,34,55,66]
# Let's plot the data
plt.plot(x, y,label='axis-x', color='green')
# Create the data
x = [1,3,5,7,9,11]
y = [10,18,20,30,40,50]
# Plot the data
plt.plot(x, y, label='axis-y', color='yellow')
# Add X Label on X-axis
plt.xlabel("X-label")
# Add X Label on X-axis
plt.ylabel("Y-label")
# Append the title to graph
plt.title("Multiple Python Line Graph")
# Add legend to graph
plt.legend()
# Display the plot
plt.show()


# Add the required libraries
import matplotlib.pyplot as plt
# Create the data
x = [1,3,5,7,9,11]
y = [10,18,20,30,40,50]
# Let's plot the data
plt.plot(x, y,label='axis-x', color='red')
# Create the data
x = [2,4,6,8,10,12]
y = [11,22,33,34,55,66]
# Plot the data
plt.plot(x, y, label='axis-y', color='blue')
# Add X Label on X-axis
plt.xlabel("X-label")
# Add X Label on X-axis
plt.ylabel("Y-label")
# Append the title to graph
plt.title("Multiple Python Line Graph")
# Add legend to graph
plt.legend()
# Display the plot
plt.show()


#scatter plot
# Add the essential library matplotlib
import matplotlib.pyplot as plt
# create the data
x = [2,4,6,8,10,12]
y = [11,22,33,34,55,66]
# Draw the scatter chart
plt.scatter(x, y, c='red', marker='*',alpha=1.0)
# Append the label on X-axis
plt.xlabel("X-label")
# Append the label on X-axis
plt.ylabel("Y-label")
# Add the title to graph
plt.title("Scatter Chart Sample")
# Display the chart
plt.show()


#pie plot
# Add the essential library matplotlib
import matplotlib.pyplot as plt
# create the data
papers = ["maj1","maj2","core1","core2"]
marks= [90,92,97,95]
# Plot the pie plot
plt.pie(marks,
labels=papers,
colors=['r','y','b','g'],
startangle=120,
shadow= True,
explode=(0,0.1,0,0),
autopct='%1.1f%%')
# Add title to graph
plt.title(" markstament")
# Draw the chart
plt.show()


#bar plot
#Add the essential library matplotlib
import matplotlib.pyplot as plt
# create the data
market_moves= [1,2,3,4,5]
rating_counts = [20,40,60,80,90]
# Plot the data
plt.bar(market_moves, rating_counts, color='green')
# Add X Label on X-axis
plt.xlabel(" market_moves")
# Add X Label on X-axis
plt.ylabel("moving Frequency")
# Add a title to graph
plt.title("market moving Distribution")
# Show the plot
plt.show()


#histogram plot
# Add the essential library
import matplotlib.pyplot as plt
# Create the data
emp_age = [3,8,6,4,5,5,7,3,7,5]
# Create bins for histogram
bins = [10,20,30,40,50]
# Plot the histogram
plt.hist(emp_age)
# Add X Label on X-axis
plt.xlabel("emp_age")
# Add X Label on X-axis
plt.ylabel("Frequency")
# Add title to graph
plt.title("emp_age Distribution")
# Show the plot
plt.show()


#seaborn implots
# Import the required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Create DataFrame
df=pd.DataFrame({'x':[1,2,4,6,8,10],'y':[11,22,33,44,55,66]})
# Create lmplot
sns.lmplot(x='x', y='y', data=df)
sns.lmplot(x='x', y='y', data=df, fit_reg=False)
# Show figure
plt.show()


#seaborn barplots
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Create DataFrame
df=pd.DataFrame({'x':['A','B','C','D','E','F'],'y':[15,25,35,45,55,65]})
# Create lmplot
sns.barplot(x='x', y='y', data=df)
# Show figure
plt.show()



#count plot
#Create count plot (also known as Histogram)
sns.countplot(x='salary', data=df)
# Show figure
plt.show()
sns.countplot(x='salary', data=df)
plt.show()


#Import required library
import seaborn as sns
# Read iris data using load_dataset() function
data = sns.load_dataset("iris")
# Find correlation
cor_matrix=data.corr()
# Create heatmap
sns.heatmap(cor_matrix, annot=False)
# Show figure
plt.show()