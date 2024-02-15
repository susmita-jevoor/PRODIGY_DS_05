# -*- coding: utf-8 -*-
"""TASK_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ywBwbipX2X4DcJd2MN1nWkXUfPGpghac

**PRODIGY INFOTECH INTERNSHIP**

**TASK 5**:Analyze traffic accident data to identify patterns related to road conditions, weather, and time of day. Visualize accident hotspots and contributing factors.

**DONE BY**: SUSMITA JEVOOR
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""IMPORTING THE DATASET"""

data=pd.read_csv('accident data.csv')
data

data.info()

data.describe(include='all')

data.head(10)

"""**ANALYSIS**"""

plt.figure(figsize=(8,8))
sns.countplot(x='Accident_Severity',data=data,hue='Urban_or_Rural_Area')
plt.title('Accident Severity by Area of Accident')
plt.xlabel('Accident Severity')
plt.ylabel('Number of Accidents')
plt.show()

light_conditions_counts=data['Light_Conditions'].value_counts()
print(light_conditions_counts)

plt.figure(figsize=(10,8))
sns.barplot(x=light_conditions_counts.index, y=light_conditions_counts.values)
plt.title('Distribution of Accidents by Light Conditions')
plt.xlabel('Light Conditions')
plt.ylabel('Number of Accidents')
plt.show()

plt.figure(figsize=(10,8))
sns.countplot(x='Accident_Severity', data=data,hue='Light_Conditions')
plt.title(' Accident Severity by Light Conditions')
plt.xlabel('Accident Severity')
plt.ylabel('Number of Accidents')
plt.show()

"""**TIME ANALYSIS**"""

data['Accident Date']=pd.to_datetime(data['Accident Date'])
data['Month']=data['Accident Date'].dt.month
plt.figure(figsize=(12,6))
sns.countplot(x='Month',data=data,hue='Accident_Severity')
plt.title(' Accident by Month')
plt.xlabel('Month')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10,8))
sns.countplot(x='Accident_Severity',data=data,hue='Road_Surface_Conditions')
plt.title('Accident Severity by Road Surface Condition')
plt.xlabel('Accident Severity')
plt.ylabel('Number of Accidents')
plt.show()

plt.figure(figsize=(10,6))
sns.countplot(x='Weather_Conditions',data=data,palette='viridis')
plt.title('Distribution of Weather Conditions')
plt.xlabel('Weather Conditions')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(x='Accident_Severity',y='Number_of_Vehicles',data=data,palette='pastel')
plt.title('Box Plot of Number of Vehicles Involved by Accident Severity')
plt.xlabel('Accident Severity')
plt.ylabel('Number of Vehicles')
plt.show()

"""***Inference:-***
The number of vehicles involved in accidents tends to increase with the severity of the accident. This is likely because more serious accidents often involve multiple vehicles colliding with each other, while slight accidents may only involve two vehicles.

The distribution of the number of vehicles involved in accidents is relatively symmetrical for all three severities. There are a few outliers in each of the severity categories.These outliers could be due to factors such as chain-reaction accidents or accidents involving large trucks or buses.
"""

plt.figure(figsize=(10,8))
columns=['Latitude','Longitude','Number_of_Casualties','Number_of_Vehicles','Month']
correlation_matrix=data[columns].corr()
sns.heatmap(correlation_matrix,annot=True,cmap='coolwarm',linewidths=.5)
plt.title('Correlation Matrix')
plt.show()