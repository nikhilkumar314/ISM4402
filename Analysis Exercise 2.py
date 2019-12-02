#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Location = "axisdata.csv"
df=pd.read_csv(Location)
df.head()


# In[2]:


df ['Cars Sold'].mean()


# In[3]:


df ['Cars Sold'].max()


# In[4]:


df ['Cars Sold'].min()


# In[5]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[6]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[8]:


df['Years Experience'].mean()


# In[9]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[10]:


pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[21]:


pd.pivot_table(df, values=['Cars Sold'], index=['Hours Worked'])


# In[17]:


pd.pivot_table(df, values=['Hours Worked'], index=['Gender'])


# In[ ]:




