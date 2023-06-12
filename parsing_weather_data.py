#!/usr/bin/env python
# coding: utf-8
import requests
import json
import csv

URL = 'https://archive-api.open-meteo.com/v1/archive'

def get_data(latitude, longitude, start_date, end_date):
    parameters = {
    'latitude' : latitude,
    'longitude' : longitude,
    'start_date' : start_date,
    'end_date' : end_date,
    'hourly' : 'temperature_2m,relativehumidity_2m,surface_pressure,precipitation,cloudcover,'
                 'direct_radiation,diffuse_radiation,windspeed_10m',
    'timezone' : 'auto'
    }
    #response_API = requests.get(URL, params=parameters)
    #response_API = requests.get(URL, params=parameters)
    try:
        response_API = requests.get(URL, params=parameters)
        response_API.raise_for_status()
        weather_data = response_API.json()
        hourly_data = weather_data['hourly']
        
        return hourly_data
    
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
        return None
    
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
        return None
    
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
        return None
    
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)
        return None
        

def make_csv(file_path, data):
    if data is None:
        print("No weather data to save.")
        return None
    
    else:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['time', 'temperature_2m', 'relativehumidity_2m', 'surface_pressure', 
                             'precipitation', 'cloudcover', 'direct_radiation', 'diffuse_radiation', 'windspeed_10m'])
        
            for i in range(len(data['time'])):
                row= [
                    data['time'][i][11:13],
                    data['temperature_2m'][i],
                    data['relativehumidity_2m'][i],
                    data['surface_pressure'][i],
                    data['precipitation'][i],
                    data['cloudcover'][i],
                    data['direct_radiation'][i],
                    data['diffuse_radiation'][i],
                    data['windspeed_10m'][i]
                ]
                writer.writerow(row)

