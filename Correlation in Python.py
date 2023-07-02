#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries

import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None

# Reading in the data
df = pd.read_csv(r'C:\Users\Sulav\Desktop\Python\movies.csv')


# In[2]:


#Looking at the data

df.head()


# In[13]:


# To see any missing data

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))


# In[14]:


# Data type for columns

print(df.dtypes)


# In[18]:


#

df['budget'] = pd.to_numeric(df['budget'], errors='coerce').fillna(0).astype(int)
df['gross'] = pd.to_numeric(df['gross'], errors='coerce').fillna(0).astype(int) 
df['votes'] = pd.to_numeric(df['votes'], errors='coerce').fillna(0).astype(int)



# In[19]:


df


# In[ ]:





# In[23]:


#Sorting data by highest gross

df.sort_values(by=['gross'], inplace=False, ascending=False)


# In[ ]:





# In[22]:


#
pd.set_option('display.max_rows', None)


# In[24]:


#Dropping duplicates

df['company'].drop_duplicates().sort_values(ascending=False)


# In[ ]:





# In[27]:


# Scatter plot with budget vs gross

# Filtering out negative budget and gross values

filtered_data = df[(df['budget'] >= 0) & (df['gross'] >= 0)]

plt.scatter(x=filtered_data['budget'], y=filtered_data['gross'])
plt.title('Budget vs Gross Earnings')
plt.xlabel('Budget For Film')
plt.ylabel('Gross Earnings')
plt.show()


# In[ ]:





# In[33]:


#
sns.regplot(x='budget',y='gross',data=filtered_data, scatter_kws={"color": "red"}, line_kws={"color":"green"})


# In[ ]:





# In[37]:


correlation_matrix = filtered_data.corr()

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix for Numeric Features")

plt.xlabel("Movie features")

plt.ylabel("Movie features")

plt.show()


# In[ ]:





# In[ ]:


df_numerized = df



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




