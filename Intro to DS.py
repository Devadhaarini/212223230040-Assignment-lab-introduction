#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data={'Name':['Jai','Princi','Gaurav','Anuj'],'Age':[27,24,22,32],'Address':['Delhi','Kanpur','Allahabad','Kannauj']}
df=pd.DataFrame(data)
print(df)
df.rename(columns={'Address':'place'},inplace=True)
print(df)


# In[2]:


import pandas as pd
df=pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
df2=pd.DataFrame([[5,6],[7,8]],columns=['a','b'])
df=pd.concat([df,df2])
print(df)


# In[3]:


import pandas as pd
data={'Name':['Jai','Princi','Gaurav','Anuj'],'Age':[27,24,22,32],'Address':['Delhi','Kanpur','Allahabad','Kannauj']}
df=pd.DataFrame(data)
df
df.drop(0,axis=0,inplace=True)
df


# In[4]:


import pandas as pd
data={'name':['Alice','Bob','Charlie','Dave'],'age':[25,32,18,47],'gender':['F','M','M','M'],'height':[1.62,1.78,1.65,1.83]}
df=pd.DataFrame(data)
df=df['name']
print(df)


# In[5]:


import pandas as pd
data={'Name':['jai','anuj'],'Age':[12,25],'Address':['Delhi','Kanpur'],'Qualification':['Msc','MA']}
df=pd.DataFrame(data)
print(df[['Name','Qualification']])


# In[6]:


import pandas as pd
data={'Name':['jai','anuj'],'Age':[12,25],'Address':['Delhi','Kanpur'],'Qualification':['Msc','MA']}
df=pd.DataFrame(data)
df.filter(items=['Name','Age'])


# In[7]:


import pandas as pd
data={'Name':['Alice','Bob','Charlie','Dave'],'age':[25,56,23,42],'gender':['F','M','M','M'],'height':[1.62,1.78,1.65,1.83]}
df=pd.DataFrame(data)
df.filter(regex='e|a',axis=1)


# In[8]:


import pandas as pd
data={'name':['Alice','Bob','Charlie','Alice'],'age':[25,56,23,42],'gender':['F','M','M','M'],'height':[1.62,1.78,1.65,1.83]}
df=pd.DataFrame(data)
df=df.drop_duplicates()
df


# In[9]:


import pandas as pd
data={'name':['Alice','Bob','Charlie','Alice'],'age':[25,56,23,42],'salary':[5000,600000,80000,200000]}
df=pd.DataFrame(data)
top_salaries=df.nlargest(2,columns='salary')
print(top_salaries)


# In[10]:


import pandas as pd
data={'name':['Alice','Bob','Charlie','Alice'],'age':[25,56,23,42],'salary':[5000,600000,80000,200000]}
df=pd.DataFrame(data)
top_salaries=df.nsmallest(2,columns='salary')
print(top_salaries)


# In[11]:


import pandas as pd
data={'name':['Alice','Bob','Charlie','Alice'],'age':[25,56,23,42],'gender':['F','M','M','M'],'height':[1.62,1.78,1.65,1.83]}
df=pd.DataFrame(data)
df=df.query('age >= 30')
print(df)


# In[12]:


import pandas as pd
data={'name':['Alice','Bob','Charlie','Alice'],'age':[25,56,23,42],'gender':['F','M','M','M'],'height':[1.62,1.78,1.65,1.83]}
df=pd.DataFrame(data)
df=df.query('name.str.contains("e") and height > 1.7')
print(df)


# In[13]:


import pandas as pd
data={'name':['Alice','Bob','Charlie','Alice'],'age':[25,56,23,42],'gender':['F','M','M','M'],'height':[1.62,1.78,1.65,1.83]}
df=pd.DataFrame(data)
df=df.query('gender == ["F","M"] and height > 1.7')
print(df)


# In[14]:


import pandas as pd
data={'name':['Alice','Bob','Charlie','Alice'],'age':[25,56,23,42],'gender':['F','M','M','M'],'height':[1.62,1.78,1.65,1.83]}
df=pd.DataFrame(data)
df.loc[:,'age']


# In[15]:


import pandas as pd
data={'name':['Alice','Bob','Charlie','Alice'],'age':[25,56,23,42],'gender':['F','M','M','M'],'height':[1.62,1.78,1.65,1.83]}
df=pd.DataFrame(data)
df.iloc[:,1]


# In[16]:


import pandas as pd
data={'name':['Alice','Bob','Charlie','Alice'],'age':[25,56,23,42],'gender':['F','M','M','M'],'height':[1.62,1.78,1.65,1.83]}
df=pd.DataFrame(data)
df.loc[:,['name','age']]


# In[17]:


import pandas as pd
data={'name':['Alice','Bob','Charlie','Alice'],'age':[25,56,23,42],'gender':['F','M','M','M'],'height':[1.62,1.78,1.65,1.83]}
df=pd.DataFrame(data)
df.iloc[:,0]


# In[18]:


import pandas as pd
data={'name':['Alice','Bob','Charlie','Alice'],'age':[25,56,23,42],'gender':['F','M','M','M'],'height':[1.62,1.78,1.65,1.83]}
df=pd.DataFrame(data)
df_filtered=df[df['age']>30]
print(df_filtered)


# In[19]:


import pandas as pd
data={'name':['Alice','Bob','Charlie','Alice'],'age':[25,56,23,42],'gender':['F','M','M','M'],'height':[1.62,1.78,1.65,1.83]}
df=pd.DataFrame(data)
df_filtered=df[(df['gender']=='M') & (df['height']>1.7)]
print(df_filtered)


# In[20]:


import pandas as pd
data={'name':['Alice','Bob','Charlie','Alice'],'age':[25,56,23,42],'gender':['F','M','M','M'],'height':[1.62,1.78,1.65,1.83]}
df=pd.DataFrame(data)
df_filtered=df[df['name'].str.startswith(('A','C'))]
print(df_filtered)


# In[21]:


import pandas as pd
data={'Name':['John','Sarah','Mike','Emily','David'],'Age':[25,31,29,35,27],'Gender':['M','F','M','F','M'],'Salary':[50000,70000,60000,80000,55000]}
df=pd.DataFrame(data)
print(df.tail(3))


# In[22]:


import pandas as pd
data={'Name':['John','Sarah','Mike','Emily','David'],'Age':[25,31,29,35,27],'Gender':['M','F','M','F','M'],'Salary':[50000,70000,60000,80000,55000]}
df=pd.DataFrame(data)
print(df.head(3))


# In[23]:


import pandas as pd
data={'Name':['John','Sarah','Mike','Emily','David'],'Age':[25,31,29,35,27],'Gender':['M','F','M','F','M'],'Salary':[50000,70000,60000,80000,55000]}
df=pd.DataFrame(data)
df.info()


# In[24]:


import pandas as pd
data={'Name':['John','Sarah','Mike','Emily','David'],'Age':[25,31,29,35,27],'Gender':['M','F','M','F','M'],'Salary':[50000,70000,60000,80000,55000]}
df=pd.DataFrame(data)
print(df.describe())


# In[25]:


import pandas as pd
data={'Name':['John','Sarah','Mike','Emily','David'],'Age':[25,31,29,35,27],'Score':[90,80,85,95,78]}
df=pd.DataFrame(data)
df_sorted=df.sort_values(by='Age',ascending=False)
print(df_sorted)


# In[26]:


import pandas as pd
data={'Name':['jai','anuj','Mano','Nan','Alice'],'age':
[24,26,24,26,24],'salary':[20000,30000,50000,90000,70000],'gender':
['M','F','M','M','F']}
df=pd.DataFrame(data)
group=df.groupby('gender').mean()['salary']
print(group)


# In[ ]:




