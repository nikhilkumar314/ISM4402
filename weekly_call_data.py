#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
import glob

all_data = pd.DataFrame()
for f in glob.glob("weekly_call_data/weekdata*.xlsx"):
    print (f)
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
    
all_data.describe()


# In[ ]:




