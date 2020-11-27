from datetime import datetime, timedelta
from tkinter import Tk, TOP, X, IntVar, StringVar, BooleanVar
from tkinter.ttk import Label, Entry, Button, Frame, Combobox, Radiobutton, Checkbutton


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
        if self.city == 'México' or str(combo_cities.get()) == '':
            return f'La hora en México es {local_time.hour}:{local_time.minute}:{local_time.second}'
        else:
            delta = self.cities[self.city]
            time_zone = timedelta(hours=delta)
            city_time = local_time + time_zone
            return f'La hora en {self.city} es {city_time.hour}:{city_time.minute}:{city_time.second}'

    def set_city(self, city_name):
        self.city = city_name


class Alarm():
    sound = ['ringbell', 'doorbell', 'Forest melody']
    duration = 0
    blink = True
    name = ''
    interval = 0

    def turn_on(self):
      # Enciende la alarma

    def turn_off(self):
      # Apaga la alarma

    def set_alarm(self):
      # Configura una nueva alarma

    def del_alarm(self):
      # Elimina una alarma

    def modify_alarm(self, alarm):
      # Modifica parámetros de una alarma existente

    def suspend(self, minutes):
      # Suspende la alarma por 'minutes' minutos


my_clock = Clock()


# def show_clock():


def update_clock(event):
    print(str(combo_cities.get()))
    lbl_clock = Label(frm_clock)
    my_clock.set_city(str(combo_cities.get()))  # setter
    lbl_clock.configure(text=my_clock.get_hour())  # getter
    lbl_clock.pack(side=TOP)


def add_new_city(event):
    values = list(combo_cities['values'])
    combo_cities['values'] = values + [str(entry_city.get())]
    print(combo_cities.current())


def delete_city(event):
    values = list(combo_cities['values'])
    values.remove(str(entry_city_del.get()))
    combo_cities['values'] = values


def update_city(event):
    values = list(combo_cities['values'])
    values[values.index(combo_cities.get())] = entry_city_update.get()
    combo_cities['values'] = values
    print(combo_cities.current())


root = Tk()
root.geometry('400x200')
root.title('Hora mundial')

frm_city = Frame(root)
lbl_write_city = Label(
    root, text="Escribe una ciudad (Madrid, Moscú, México, Nueva York, Tokio)")
lbl_write_city.pack(side=TOP)

# Wiget Combobox
combo_cities = Combobox(frm_city, state='readonly')
combo_cities['values'] = ('Madrid', 'México', 'Moscú', 'Nueva York', 'Tokio')
combo_cities.current(1)
combo_cities.bind('<<ComboboxSelected>>', update_clock)
combo_cities.pack()

# btn_set_city = Button(text='Ver hora', command=show_clock)
# btn_set_city.pack(side=TOP, after=combo_cities)
frm_city.pack(fill=X)

Label(root, text="Escribe el nombre de la ciudad a agregar y presiona <Enter>").pack()
entry_city = Entry(root)
entry_city.bind('<Return>', add_new_city)
entry_city.pack(side=TOP, fill=X, expand=1)
# btn_add_new_city = Button(
#     root, text='Agregar nueva ciudad', command=add_new_city)
# btn_add_new_city.pack()

Label(root, text="Escribe el nombre de la ciudad a eliminar y presiona <Enter>").pack()
entry_city_del = Entry(root)
entry_city_del.bind('<Return>', delete_city)
entry_city_del.pack(side=TOP, fill=X, expand=1)
# btn_del_new_city = Button(
#     root, text='Eliminar ciudad', command=delete_city)
# btn_del_new_city.pack()

Label(root, text="Escribe el nombre de la ciudad a actualizar y presiona <Enter>").pack()
entry_city_update = Entry(root)
entry_city_update.bind('<Return>', update_city)
entry_city_update.pack(side=TOP, fill=X, expand=1)
# btn_update_new_city = Button(
#     root, text='Actualizar nombre de ciudad', command=update_city)
# btn_update_new_city.pack()


def show_selected():
    if opt.get() == 0:
        # print(f'Buenos dias!')
        frm_sports.pack()
        # hard coding
        op1_value.set(False)
        op2_value.set(False)
        op3_value.set(False)
        op4_value.set(False)
    else:
        # print(f'Buenas tardes!')
        frm_sports.pack_forget()


opt = IntVar()
# Widget Radiobutton
Label(root, text='¿Te gustan los deportes?').pack()
rad_am = Radiobutton(root, text='Sí', value=0,
                     command=show_selected, variable=opt)
rad_am.pack()
rad_pm = Radiobutton(root, text='No', value=1,
                     command=show_selected, variable=opt)
rad_pm.pack()

# Widget Checkbox (Checkbutton)


def show_check_selected():
    if op1_value.get():
        print('Opción 1 está seleccionada')
    else:
        print('Opción 1 NO está seleccionada')
    if op2_value.get():
        print('Opción 2 está seleccionada')
    else:
        print('Opción 2 NO está seleccionada')


op1_value = BooleanVar()
op2_value = BooleanVar()
op3_value = BooleanVar()
op4_value = BooleanVar()

print(op1_value, op2_value)
frm_sports = Frame(root)
Label(frm_sports, text='Selecciona todos tus deportes preferidos:').pack()
chk_op1 = Checkbutton(frm_sports, text='Fútbol', var=op1_value,
                      command=show_check_selected)
chk_op1.pack()

chk_op2 = Checkbutton(frm_sports, text='Básquetbol', var=op2_value,
                      command=show_check_selected)
chk_op2.pack()

chk_op3 = Checkbutton(frm_sports, text='Béisbol', var=op3_value,
                      command=show_check_selected)
chk_op3.pack()

chk_op4 = Checkbutton(frm_sports, text='Golf', var=op4_value,
                      command=show_check_selected)
chk_op4.pack()


frm_clock = Frame(root)
frm_clock.pack(fill=X)

root.mainloop()
