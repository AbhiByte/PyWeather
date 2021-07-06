from tkinter import *
import requests

api_address = 'https://api.openweathermap.org/data/2.5/weather?appid={yourID}&q='
city = input("Enter city name: ")
url = api_address + city
try:
    json_data = requests.get(url).json()
except Exception as e:
    json_data = "Error"

temp = round(float(json_data['main']['temp']) - 273.15, 1)
weather = (json_data['weather'][0]['description'])

#Window
window = Tk()
window.title('Weather Report')
window.geometry('500x500')

def search():
    pass

city_entry = Entry(window, textvariable='')
city_entry.pack()
search_button = Button(window, text='Search Weather', width=12, command=search)
search_button.pack()

tempLabel = Label(window, text=f'The current temperature is: {temp} °C', font=("Times New Roman", 20))
tempLabel.pack()
weatherLabel = Label(window, text=f'The current weather is: {weather}', font=("Times New Roman", 20))
weatherLabel.pack()

window.mainloop()
