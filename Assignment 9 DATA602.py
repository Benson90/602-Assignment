#!/usr/bin/env python
# coding: utf-8

# ## Assignment #9
# In this assignment, you will practice using the plotly express library.
# https://plotly.com/python/plotly-express/
# Your goal is to recreate the following graphics below using plotly express. You should attempt to recreate them as closely as possible.

# In[34]:


import plotly.express as px
df = px.data.tips()
df.head()


# ## Bar Plot
# A barplot shows the relationship between a numeric and a categorical variable. Each entity of the categoric variable is represented as a bar. The size of the bar represents its numeric value.

# In[35]:


fig_bar = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group")
fig_bar.show()


# In[36]:


fig_bar = px.bar(df, x="sex", y="total_bill", color="day", barmode="group")
fig_bar.show()


# ## Scatter Plot
# Scatter plots are used to check the relationship between the variables and the distribution of the data. A scatterplot displays the relationship between 2 numeric variables. For each data point, the value of its first variable is represented on the X axis, the second on the Y axis

# In[37]:


fig_scatter = px.scatter(df, x="total_bill", y="tip", facet_col ="smoker", color="sex")
fig_scatter.show()


# In[38]:


fig_scatter = px.scatter(df, x="total_bill", y="tip", facet_col ="smoker", color="sex", trendline="ols")
fig_scatter.show()


# In[39]:


fig_scatter = px.scatter(df, x="total_bill", y="tip", facet_col ="day", facet_row="time", category_orders={"day": ["Thur", "Fri", "Sat", "Sun"], "time": ["Dinner", "Lunch"]})
fig_scatter.show()


# ## Histogram
# 
# A histogram takes as input a numeric variable only. The variable is cut into several bins, and the number of observation per bin is represented by the height of the bar. It is possible to represent the distribution of several variable on the same axis using this technique.

# In[40]:


fig_histogram = px.histogram(df, x="tip", marginal="rug", hover_data=df.columns)
fig_histogram.show()


# ## Boxplot
# 
# A boxplot gives a nice summary of one or several numeric variables. The line that divides the box into 2 parts represents the median of the data

# In[41]:


fig_box = px.box(df, x="smoker", y="tip", color="smoker")
fig_box.show()


# In[ ]:




