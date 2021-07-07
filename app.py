from tkinter import *
import requests

#Window
window = Tk()
window.title('Weather Report')
window.geometry('500x500')

def getWeather(window):
    city = city_entry.get()
    api_address = 'https://api.openweathermap.org/data/2.5/weather?appid={yourID}&q='
    url = api_address + city
    try:
        json_data = requests.get(url).json()
    except Exception as e:
        json_data = "Error"
    temp = round(float(json_data['main']['temp']) - 273.15, 1)
    weather = (json_data['weather'][0]['description'])

    tempLabel.config(text = f'The current temperature is: {temp} °C', font=("Times New Roman", 20))
    weatherLabel.config(text = f'The current weather is: {weather}', font=("Times New Roman", 20))



city_entry = Entry(window, textvariable='')
city_entry.pack()
city_entry.focus()
city_entry.bind('<Return>', getWeather)


tempLabel = Label(window)
tempLabel.pack()
weatherLabel = Label(window)
weatherLabel.pack()

window.mainloop()
