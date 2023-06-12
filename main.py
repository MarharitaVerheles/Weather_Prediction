#!/usr/bin/env python
# coding: utf-8

from parsing_weather_data import get_data, make_csv
from weather_prediction import predictio

data = get_data(49.98, 36.25, '2022-06-07', '2023-06-07')
file_path = 'weather_data_from_api.csv'
make_csv(file_path, data)
user_data = [7, 12, 56.25, 1008, 23, 81.95, 129.91, 9.67]
prediction(user_data)

