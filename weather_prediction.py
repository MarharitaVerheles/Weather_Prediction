#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def prediction(user_data):
    data = pd.read_csv('weather_data_from_api.csv')
    data = data.dropna()
    data = data.fillna(data.mean())
    
    columns = ['time', 'temperature_2m', 'relativehumidity_2m', 'surface_pressure', 
                 'cloudcover', 'direct_radiation', 'diffuse_radiation', 'windspeed_10m']
    
    train, test = train_test_split(data, test_size=0.25, random_state=42)
    
    x_train = train[columns]
    x_test = test[columns]
    
    y_train = train['precipitation']
    y_test = test['precipitation']
    
    model = LinearRegression()
    model.fit(x_train, y_train)
    
    y_pred = model.predict(x_test)
    mse = mean_squared_error(y_test, y_pred)
    
    print('Середьоквадратичн похибка: {}'.format(mse))
    x, y = zip(*sorted(zip(y_pred, y_test)))

    plt.plot(x, y)
    plt.plot([0, 2], [0, 2], '--r')
    plt.xlabel('Prediction')
    plt.ylabel('Real values')
    plt.show()
    
    user_data = np.array(user_data).reshape(1, -1)
    
    new_data = pd.DataFrame(
        {
        "time": [user_data[0, 0]], 
        "temperature_2m":[user_data[0, 1]],
        "relativehumidity_2m": [user_data[0, 2]],
        "surface_pressure": [user_data[0, 3]], 
        "cloudcover": [user_data[0, 4]],
        "direct_radiation": [user_data[0, 5]],
        "diffuse_radiation": [user_data[0, 6]], 
        "windspeed_10m":[ user_data[0, 7]]
        }
    )
    return model.predict(user_data)

