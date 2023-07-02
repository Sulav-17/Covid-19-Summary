#!/usr/bin/env python
# coding: utf-8

# In[23]:


import os, shutil 


# In[24]:


path = r"C:/Users/Sulav/Desktop/Power Bi/"


# In[25]:


file_name = os.listdir(path)


# In[26]:


folder_names = ['Excel files', 'Pdf files', 'Power bi files']


for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs((path + folder_names[loop]))
        
for file in file_name:
    if ".xlsx" in file and not os.path.exists(path + "Excel files/" + file):
        shutil.move(path + file, path + "Excel files/" + file)
    elif ".pbix" in file and not os.path.exists(path + "Power bi files/" + file):
        shutil.move(path + file, path + "Power bi files/" + file)   
    elif ".pdf" in file and not os.path.exists(path + "Pdf files/" + file):
        shutil.move(path + file, path + "Pdf files/" + file)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




