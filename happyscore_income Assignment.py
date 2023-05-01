#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv("happyscore_income.csv")
df.head(150)


# In[3]:


df["region"].value_counts()


# In[5]:


df.describe()


# In[11]:


df.plot(kind="scatter", x="avg_satisfaction", y="avg_income")


# In[12]:


df.plot(kind="scatter", x="std_satisfaction", y="avg_income")


# In[15]:


sns.FacetGrid(df, hue="country", size=5)    .map(plt.scatter, "avg_satisfaction","avg_income")    .add_legend()


# In[ ]:


sns.pairplot(df.drop("std_satisfaction", axis=1), hue="country", size=3)


# In[ ]:




