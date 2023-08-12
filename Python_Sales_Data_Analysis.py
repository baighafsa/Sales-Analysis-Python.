#!/usr/bin/env python
# coding: utf-8

# # Sales Analysis

# ### Import required libraries

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# ### Read data set

# In[4]:


import pandas as pd
df=pd.read_csv(r'C:\Users\SPECTRE\Desktop\DataAnalysis_DataSets\Sales_Analysis\Sales_Data.csv' , header= 0,
                        encoding= 'unicode_escape')


# In[5]:


df


# In[7]:


df.shape


# In[8]:


df.head()


# In[9]:


df.info()


# In[11]:


df.drop(['Status','unnamed1'], axis=1, inplace=True)
#drop blank columns


# In[12]:


df.info()


# In[13]:


pd.isnull(df)


# In[14]:


pd.isnull(df).sum() # check for null values


# In[15]:


df.shape


# In[16]:


#drop null values
df.dropna(inplace=True)


# In[17]:


pd.isnull(df).sum()


# In[21]:


df['Amount']=df['Amount'].astype('int')


# In[22]:


df['Amount'].dtypes


# In[23]:


df.columns


# In[24]:


#rename columns
df.rename(columns={'Marital_Status':'Married'})


# In[25]:


#statistics
df.describe()


# In[26]:


df[['Age','Orders','Amount']].describe()


# ## Explorartory Data Analysis

# ### Gender

# In[27]:


df.columns


# In[29]:


ax = sns.countplot(x='Gender',data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[31]:


sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sales_gen


# In[32]:


sns.barplot(x='Gender' , y='Amount' ,data=sales_gen)


# ### Age

# In[33]:


ax=sns.countplot(data = df, x='Age Group', hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# ### State

# In[35]:


# total number of orders from top 10 states
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state, x='State', y='Orders')


# In[36]:


# total amount/sales from top 10 states
sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)}) #height width
sns.barplot(data=sales_state, x='State', y='Amount')


# ### Marital Status:

# In[42]:


ax= sns.countplot(data=df, x='Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[44]:


sales_state = df.groupby(['Marital_Status','Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data=sales_state, x='Marital_Status', y='Amount',hue='Gender')


# ### Occupation

# In[52]:


ax= sns.countplot(data=df, x='Occupation')

sns.set(rc={'figure.figsize':(30,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[47]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x='Occupation', y='Amount')


# ### Product Category

# In[51]:


ax= sns.countplot(data=df, x='Product_Category')

sns.set(rc={'figure.figsize':(30,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[49]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x='Product_Category', y='Amount')


# ## Insights:
# #### Married women in the age group 26-35 yrs from UP, Maharashtra and Karnataka working in IT, Healthcare and aviation are more likely to buy products from food, clothing and electronics category.
# 

# In[ ]:




