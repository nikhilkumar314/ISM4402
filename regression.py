#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
location = "datasets/gradedata.csv"
df= pd.read_csv(location)
df.head()


# In[15]:


def gen_to_num(x):
    if x == 'female':
        return 1
    if x == 'male':
        return 0


# In[17]:


df['gender_val'] = df['gender'].apply(gen_to_num)
df.tail()


# In[19]:


import statsmodels.formula.api as sm
result = sm.ols(formula= 'grade ~ age + exercise + hours + gender_val', data=df).fit()
result.summary()


# In[20]:


import statsmodels.formula.api as sm
result = sm.ols(formula= 'grade ~ exercise + hours + gender_val', data=df).fit()
result.summary()


# In[ ]:




