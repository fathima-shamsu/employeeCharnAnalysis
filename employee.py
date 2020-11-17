# this proj :Employee Churn Analysis
#Exploratory Data Analysis is an initial process of analysis, in which you can summarize characteristics of data such as pattern, trends, outliers, and hypothesis testing using descriptive statistics and visualization.
#pandas: for dataframes
import pandas 
#matplotlib: for plotting graphs
import matplotlib.pyplot as plt 
 #seaborn: for plotting graphs
import seaborn as sns
#dataset : set path of downloaded dataset
data=pandas.read_csv(r"C:\Users\DELL\Downloads\HR_comma_sep.csv")

data.head()
#tail() returns last five observations
data.tail()
#get attributes names and datatypes using: .info()
data.info()

#In the given dataset, we have two types of employee one who stayed and another who left the company. So, you can divide data into two groups and compare their characteristics. Here, we can find the average of both the groups using groupby() and mean() function
left = data.groupby('left')
left.mean()
#Here we can interpret, Employees who left the company had low satisfaction level, low promotion rate, low salary, and worked more compare to who stayed in the company.

#describe() :returns the count, mean, standard deviation, minimum and maximum values and the quantiles of the data.
data.describe()

#-----------data visualisation -------------
left_count=data.groupby('left').count()
plt.bar(left_count.index.values, left_count['satisfaction_level'])
plt.xlabel('Employees Left Company')
plt.ylabel('Number of Employees')
plt.show()
data.left.value_counts()