#!/usr/bin/env python
# coding: utf-8
# In[1]:
from parsing_weather_data import get_data, make_csv
from weather_prediction import predictio
# In[2]:
data = get_data(49.98, 36.25, '2022-06-07', '2023-06-07')
# In[3]:
file_path = 'weather_data_from_api.csv'
# In[4]:
make_csv(file_path, data)
# In[ ]:
user_data = [7, 12, 56.25, 1008, 23, 81.95, 129.91, 9.67]
prediction(user_data)

