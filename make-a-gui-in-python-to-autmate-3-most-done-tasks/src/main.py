#!/bin/env python
import tkinter as tk
import webbrowser
from weather import Weather
from time import ctime


def open_youtube_music():
    webbrowser.open('https://music.youtube.com/')


def open_messenger():
    webbrowser.open('https://messenger.com')


class Window(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.check_weather = tk.Button(self.master)
        self.check_weather.grid(row=0, column=0)
        self.check_weather['text'] = "Check current weather"
        self.check_weather['command'] = self.print_weather

        self.ytmusic = tk.Button(self.master)
        self.ytmusic.grid(row=0, column=1)
        self.ytmusic['text'] = "Open YouTube Music"
        self.ytmusic['command'] = open_youtube_music

        self.messenger = tk.Button(self.master)
        self.messenger.grid(row=0, column=2)
        self.messenger['text'] = "Open Facebook Messenger"
        self.messenger['command'] = open_messenger

    def print_weather(self):
        tk.Label(self.master, text=f'Weather in {CITYNAME}:').grid(row=1, column=0)
        tk.Label(self.master, text='Description:').grid(row=2, column=0)
        tk.Label(self.master, text='Temperature:').grid(row=3, column=0)
        tk.Label(self.master, text='Wind speed:').grid(row=4, column=0)
        tk.Label(self.master, text='Sunrise:').grid(row=5, column=0)
        tk.Label(self.master, text='Sunset:').grid(row=6, column=0)
        tk.Label(self.master, text='Humidity').grid(row=7, column=0)
        tk.Label(self.master, text='Pressure').grid(row=8, column=0)

        weather = Weather(API_KEY)
        weather_data = weather.get_by_city_name(CITYNAME, units='metric')

        tk.Label(self.master, text=weather_data['weather'][0]['description']).grid(row=2, column=1)
        tk.Label(self.master, text=f"{weather_data['main']['temp']} °C").grid(row=3, column=1)
        tk.Label(self.master, text=f"{weather_data['wind']['speed']} m/s").grid(row=4, column=1)
        tk.Label(self.master, text=ctime(weather_data['sys']['sunrise'])).grid(row=5, column=1)
        tk.Label(self.master, text=ctime(weather_data['sys']['sunset'])).grid(row=6, column=1)
        tk.Label(self.master, text=f"{weather_data['main']['humidity']} %").grid(row=7, column=1)
        tk.Label(self.master, text=f"{weather_data['main']['pressure']} hPa").grid(row=8, column=1)


if __name__ == "__main__":
    API_KEY = "9fa16bd5078ca8dffdf54339845e08e6"
    CITYNAME = "Gizycko"
    root = tk.Tk()
    root.title = "Automator by SynneK1337"
    window = Window(master=root)
    window.mainloop()
