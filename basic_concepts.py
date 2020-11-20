from datetime import datetime, timedelta
from tkinter import Tk, TOP, X
from tkinter.ttk import Label, Entry, Button, Frame

# Misión:
# Crear una clase que permita crear relojes con distintos husos horarios para las siguientes
# ciudades:
# Madrid, Tokio, Moscú, Centro de la CDMX, Nueva York
# y que permita visualizar la hora actual CORRECTA de las distintas ciudades
# hora_madrid = Reloj()
# hora_madrid.set_city('Madrid')
# hora_madrid.get_hour()  # La hora en Madrid es: 18:31:55


class Clock():
    city = ''
    time_zone = 0
    cities = {
        'Madrid': 7,
        'Nueva York': 1,
        'Tokio': 15,
        'Moscú': 9
    }

    # Método constructor
    def __init__(self, city='México'):
        if not (city) in self.cities:
            self.city = 'México'
        else:
            self.city = city

    def get_hour(self):
        local_time = datetime.now()
        if self.city == 'México':
            return f'La hora en México es {local_time.hour}:{local_time.minute}:{local_time.second}'
        else:
            delta = self.cities[self.city]
            time_zone = timedelta(hours=delta)
            city_time = local_time + time_zone
            return f'La hora en {self.city} es {city_time.hour}:{city_time.minute}:{city_time.second}'

    def set_city(self, city_name):
        self.city = city_name


my_clock = Clock()


def show_clock():
    lbl_clock = Label(frm_clock)
    my_clock.set_city(str(entry_city.get()))  # setter
    lbl_clock.configure(text=my_clock.get_hour())  # getter
    lbl_clock.pack(side=TOP)


root = Tk()
root.geometry('400x200')
root.title('Hora mundial')

frm_city = Frame(root)
lbl_write_city = Label(
    root, text="Escribe una ciudad (Madrid, Moscú, México, Nueva York, Tokio)")
lbl_write_city.pack(side=TOP)
entry_city = Entry(frm_city)
entry_city.pack(side=TOP, fill=X, expand=1)
btn_set_city = Button(text='Ver hora', command=show_clock)
btn_set_city.pack(side=TOP, after=entry_city)
frm_city.pack(fill=X)

frm_clock = Frame(root)

frm_clock.pack(fill=X)

root.mainloop()
