
from cProfile import label
from email import contentmanager
from tkinter import *
from tkinter.ttk import *
import requests
root = Tk()
root.title('Weather App')
root.geometry('500x300')


def getWeather():
    city = city_text.get()
    link = 'https://api.openweathermap.org/data/2.5/weather?q=' + \
        city+'&units=metric&appid=22515dbe8047cf659da74a1cae281c2e'
    response = requests.get(link)
    data = response.json()
    placeLabel['text'] = '{}, {}'.format(data['name'], data['sys']['country'])
    tempLabel['text'] = '{} °C'.format(data['main']['temp'])


header = Label(root, text='Weather App', font=('bold', 15)).place(x=190, y=50)
citylabel = Label(root, text='Enter your city',
                  font=('bold', 10)).place(x=200, y=80)
city_text = StringVar()
city_entry = Entry(root, textvariable=city_text)
city_entry.place(x=170, y=110)
search = Button(root, text='GO', width=12, command=getWeather)
search.place(x=190, y=150)
placeLabel = Label(root, text='', font=('bold', 15))
placeLabel.place(x=190, y=180)
tempLabel = Label(root, text='', font=('bold', 15))
tempLabel.place(x=190, y=210)
root.mainloop()
