#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[8]:


bins = [0,80,100]
status_names = ['Fail' , 'Pass']
df['status'] = pd.cut(df['grade'], bins, labels=status_names)
df


# In[9]:


pd.value_counts(df['status'])


# In[ ]:




