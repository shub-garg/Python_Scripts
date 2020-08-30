# Weather GUI

import tkinter as tk
from tkinter import font
import requests

root = tk.Tk()

root.title("Weather")

canvas = tk.Canvas(root, height=400, width=600)
canvas.pack()

background_image = tk.PhotoImage(file='3108.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relheight=1, relwidth=1)

frame1 = tk.Frame(root, bg='white', cursor='arrow', bd=1)
frame1.place(relx=0.2, rely=0.15, relheight=0.1, relwidth=0.6)


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City : %s  \nCondition : %s \nTemperature (C): %s' % (name, desc, temp)
    except:
        final_str = 'Network Issue'
    return final_str


def get_weather(city):
    weather_key = 'c927d1f99052dea241d16edb226ed6ec'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


entry = tk.Entry(frame1)
entry.insert(0, "Enter City")
entry.place(relx=0.01, rely=0.08, relheight=0.84, relwidth=0.7)

button = tk.Button(frame1, text='Check', bg='#b3cccc', fg='#000000', command=lambda: get_weather(entry.get()))
button.place(relx=0.73, rely=0.08, relheight=0.84, relwidth=0.26)

frame2 = tk.Frame(root, bg='white', cursor='arrow', bd=6)
frame2.place(relx=0.2, rely=0.35, relheight=0.5, relwidth=0.6)

label = tk.Label(frame2)
label.place(relwidth=1, relheight=1)

root.mainloop()
