#!/usr/bin/env python
# coding: utf-8

# # Ecommerce Data Analysis

# In[1]:


#importing numpy for mathematical operations

import numpy as np


# In[2]:


#import pandas for manipulation ,cleaning etc

import pandas as pd


# In[3]:


#importing matplot and seaborn for data visualization

import matplotlib.pyplot as plt
import seaborn as sn


# In[4]:


#Reading the data

data=pd.read_csv("Ecommerce_Cleaning_Teest.csv")


# In[5]:


data


# In[6]:


#Shape shows the number of rows and columns
data.shape


# In[7]:


data.info()


# In[8]:


#checking the null values
data.isnull().sum()


# In[9]:


#describing the data
data.describe()


# # Data preprocessing
# 

# In[10]:


email_name_map = data[data['Customer_Name'].notna()].drop_duplicates(subset='Email')
email_name_dict = dict(zip(email_name_map['Email'], email_name_map['Customer_Name']))

# Step 3: Fill missing Customer Names using the email_name_dict
data['Customer_Name'] = data.apply(
    lambda row: email_name_dict[row['Email']] if pd.isna(row['Customer_Name']) and row['Email'] in email_name_dict else row['Customer_Name'],
    axis=1)


# In[11]:


# Step 1: Convert all values to lowercase
data['Payment_Mode'] = data['Payment_Mode'].str.lower()

# Step 2: Strip spaces (if any) and map to clean labels
data['Payment_Mode'] = data['Payment_Mode'].str.strip().replace({
    'paypal': 'Paypal',
    'credit card': 'Credit Card',
    'debit card': 'Debit Card',
    'debitcard': 'Debit Card',
    'upi payment': 'UPI Payment',
    'net banking': 'Net Banking',
    'cash': 'Cash'
})


# In[12]:


data.isnull().sum()


# In[13]:


data


# In[14]:


#Removing the null values

data.dropna(inplace=True)


# In[15]:


data.shape


# In[16]:


data.drop(['Email','Shipping_Address'],axis=1,inplace=True)


# In[17]:


data.shape


# In[18]:


data['Order_Date']=pd.to_datetime(data['Order_Date'],format='mixed',dayfirst=True ,errors='coerce')


# In[19]:


data['Order_Date'].dtype


# In[20]:


data['Delivery_Date']=pd.to_datetime(data['Delivery_Date'],format='mixed',dayfirst=True, errors='coerce')


# In[21]:


data.isnull().sum()

Univariate analysis-Focuses on one variable at a time.
# In[22]:


#countplot for order status

ax=sn.countplot(data=data , x='Order_Status')
plt.title('Order status distribution')
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{height}', (p.get_x() + p.get_width() / 2., height),
                ha='center', va='bottom')
plt.show


# In[23]:


#countplot for product category

pc=sn.countplot(data=data,x='Product_Category', order=data['Product_Category'].value_counts().index)
plt.xticks(rotation=45)
plt.title('Product Category Distribution')
for p in pc.patches:
    height = p.get_height()
    pc.annotate(f'{height}', (p.get_x() + p.get_width() / 2., height),
                ha='center', va='bottom')
plt.show()


# In[24]:


pip install --upgrade seaborn


# In[25]:


#Histogram for price

plt.hist(data['Price'], bins=40,edgecolor='black')
plt.title('Price distribution by Quantity')
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.show()


# Bivariate Analysis- Analysis contain two variables.

# In[26]:


#sales by category

sales_category=data.groupby('Product_Category')['Final_Amount'].sum().sort_values(ascending=False)
sales_category.plot(kind='bar',title='Sales by Product Category')
plt.ylabel('Total Sales')
plt.show()


# In[27]:


#Payment mode preference

sn.countplot(data=data , x='Payment_Mode' , order = data['Payment_Mode'].value_counts().index , palette='Set2')
plt.title("Payment mode distribution")
plt.xticks(rotation=45)
plt.show()


# In[28]:


# Analysing discount and final price

sn.scatterplot(x='Discount (%)',y='Final_Amount', data=data)
plt.title('Discount vs Final Amount')
plt.show()


# Customer Insights

# In[29]:


#Top customer by sales

top_customers= data.groupby('Customer_Name')['Final_Amount'].sum().sort_values(ascending= False).head(10)
top_customers.plot(kind='barh' , title='Top 10 Customers')
plt.xlabel('Final Amount')
plt.gca().invert_yaxis()
plt.show()


# Review and Return

# In[30]:


#Return rate
return_rate = data['Return_Status'].value_counts(normalize=True) * 100
print("Return Rate (%)")
print(return_rate)


# Correlation map

# In[31]:


# Correlation for numeric features
numeric_cols = data.select_dtypes(include=['float64', 'int64'])
sn.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()


# In[ ]:




