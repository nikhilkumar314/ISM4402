#!/usr/bin/env python
# coding: utf-8

# In[43]:


import matplotlib.pyplot as plt
import pandas as pd
Location = "datasets/axisdata.csv"
df=pd.read_csv(Location)
df.head()


# In[4]:


df ['Cars Sold'].mean()


# In[41]:


df ['Cars Sold'].max()


# In[44]:


df ['Cars Sold'].min()


# In[45]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[46]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[47]:


df['Years Experience'].mean()


# In[48]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[49]:


pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[51]:


pd.pivot_table(df, values=['Cars Sold'], index=['Hours Worked'])


# In[52]:


df ['Hours Worked'].mean()


# In[50]:


plt.scatter(df['Hours Worked'], df['Cars Sold'])


# In[40]:


df.boxplot (by='Gender', column='Hours Worked')


# In[53]:


pd.pivot_table(df, values=['Hours Worked'], index=['Gender'])


# In[ ]:




