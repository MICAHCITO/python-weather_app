# import requests
# API_KEY = '5cf78591cd84803b748b45de9a508364'
# BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


# def get_weather(city):
#     params = {
#         'q' : city,
#         'appid' : API_KEY,
#         'units' : 'Metric'
#     }

#     response = requests.get(BASE_URL, params = params)
#     if response.status_code == 200:
#         data = response.json()
#         weather = {
#             'name' : data['name'],
#             'temperature' : data['main']['temp'],
#             'description' : data['weather'][0]['description'],
#             'humidity' : data['main']['humidity'],
#             'wind_speed' : data['wind']['speed']
        
#         }
#         return weather
        
#     else:
#         print('Error, city not found!!')
#         return
    
# def display_weather(weather):
#     if weather:
#         print('city: {}'.format(weather['name']))
#         print('temperature: {}'.format(weather['temperature']))
#         print('description: {}'.format(weather['description']))
#         print('humidity: {}'.format(weather['humidity']))
#         print('wind_speed: {}'.format(weather['wind_speed']))
#     else:
#         print('Could not retrieve weather report')
# def run_all():
#     city = input('Enter your city: ')
#     weather = get_weather(city)
#     display_weather(weather)

# run_all()

import tkinter as tk
import requests

API_KEY = '5cf78591cd84803b748b45de9a508364'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q' : city,
        'appid' : API_KEY,
        'units' : 'metric'  # Changed to lowercase 'metric'
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'name': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return None

def display_weather(weather):
    if weather:
        result_label.config(text=f"City: {weather['name']}\n"
                                 f"Temperature: {weather['temperature']}°C\n"
                                 f"Description: {weather['description']}\n"
                                 f"Humidity: {weather['humidity']}%\n"
                                 f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        result_label.config(text="Could not retrieve weather information.")

def get_weather_and_display():
    city = city_entry.get()
    weather = get_weather(city)
    display_weather(weather)

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create GUI elements
city_label = tk.Label(root, text="Enter city:")
city_label.pack(pady=10)

city_entry = tk.Entry(root, width=30)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather_and_display)
get_weather_button.pack(pady=10)

result_label = tk.Label(root, text="", wraplength=400, justify="left")
result_label.pack(pady=20)

# Run the main tkinter event loop
root.mainloop()
