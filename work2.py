import pandas as pd 
import numpy as py
from sklearn.model_selection import train_test_split

#data loading
data=pd.read_csv("grade.csv")
print(data)

#data preprocessing
a=data.isna().sum()
print(a)

# Import label encoder
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
data['gender']= label_encoder.fit_transform(data['gender'])
data['gender'].unique()
data['race/ethnicity']= label_encoder.fit_transform(data['race/ethnicity'])
data['race/ethnicity'].unique()
data['parental level of education']= label_encoder.fit_transform(data['parental level of education'])
data['parental level of education'].unique()
data['lunch']= label_encoder.fit_transform(data['lunch'])
data['lunch'].unique()
data['test preparation course']= label_encoder.fit_transform(data['test preparation course'])
data['test preparation course'].unique()
data['result']= label_encoder.fit_transform(data['result'])
data['result'].unique()

#split the data into dependent and independent data
X=data.iloc[:,:-1]
print(X)
Y=data['result']

#split the Data into training data and testing data 
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,shuffle=True)
#apply simplified algorithm
from sklearn.linear_model import LogisticRegression
clf=LogisticRegression()
clf.fit(X_train,Y_train)
Y_predict=clf.predict(X_test)
#Prediction to find Accuracy
from sklearn.metrics import accuracy_score
print("Accuracy:",accuracy_score(Y_test,Y_predict))

from sklearn.ensemble import RandomForestClassifier
rfmodel= RandomForestClassifier()
rfmodel.fit(X_train, Y_train)
predict1=rfmodel.predict(X_test)
from sklearn.metrics import accuracy_score
print("Accuracy:", accuracy_score(Y_test,predict1))

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train, Y_train)
grade=classifier.predict(X_test)
#prediction to find accuracy
from sklearn.metrics import accuracy_score
print("Accuracy:", accuracy_score(Y_test,grade))


#line plot
#Data plotting
# Add the essential library matplotlib
import matplotlib.pyplot as plt
import numpy as np
# create the data
a = np.linspace(40, 90)
# Draw the plot
plt.plot(a)
# Display the chart
plt.show()

plt.plot(X_test,Y_test)
plt.scatter(X_test,Y_test)
plt.bar(X_test,Y_test)

import pandas as pd 
import seaborn as sns
import matplotlab as plt
import numpy as np
data=pd.read_csv("grade.csv")
sns.lineplot(data["math score"],data["writing score"])

