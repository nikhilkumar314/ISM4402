#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'datasets/gradedata.db'


# In[17]:


engine = create_engine(r"sqlite:///{}".format(db_file))


# In[18]:


sql = 'SELECT * from test where Grades in (76,77,78)'


# In[22]:


sales_data_df = pd.read_sql(sql, engine)
sales_data_df.head()


# In[24]:


sql = "select name from sqlite_master"
"where type = 'table';"


# In[26]:


sql = "select * from test;"
sales_data_df.head()


# In[ ]:




