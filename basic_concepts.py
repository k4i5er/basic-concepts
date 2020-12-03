from datetime import datetime, timedelta
from tkinter import Tk, TOP, X, IntVar, StringVar, BooleanVar, LEFT
from tkinter.ttk import Label, Entry, Button, Frame, Combobox, Radiobutton, Checkbutton


class Clock():
    alarms = []
    hours = 0
    minutes = 0
    seconds = 0

    # Método constructor
    def __init__(self):
        local_time = datetime.now()
        hours = local_time.hour
        minutes = local_time.minute
        seconds = local_time.second

    def get_hour(self):
        local_time = datetime.now()
        return f'La hora en México es {local_time.hour}:{local_time.minute}:{local_time.second}'

    def set_alarm(self, hours, minutes, seconds, sound, duration, name, interval):
        alarm = Alarm(hours, minutes, seconds, sound, duration, name, interval)
        self.alarms.append(alarm)


class Alarm():
    sound = ['ringbell', 'doorbell', 'Forest melody']
    sound_name = ''
    duration = 0
    blink = True
    name = ''
    interval = 0
    hours = 0
    minutes = 0
    seconds = 0

    def __init__(self, hours, minutes, seconds, sound, duration, name, interval):
        self.sound_name = self.sound[sound]
        self.duration = duration
        self.name = name
        self.interval = interval
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # def turn_on(self):
        # Enciende la alarma

        # def turn_off(self):
        #     # Apaga la alarma

        # def del_alarm(self):
        #     # Elimina una alarma

        # def modify_alarm(self, alarm):
        #     # Modifica parámetros de una alarma existente

        # def suspend(self, minutes):
        #     # Suspende la alarma por 'minutes' minutos

        # my_clock = Clock()


def save_alarm():
    reloj.set_alarm(entry_hour.get(), entry_minute.get(), entry_second.get(
    ), alarm_sound.get(), cmb_duration.get(), entry_name.get(), cmb_interval.get())


def set_alarm():
    global entry_name
    global entry_hour
    global entry_minute
    global entry_second
    global alarm_sound
    global cmb_interval
    global cmb_duration

    frm_alarm = Frame(root)

    Label(frm_alarm, text='Nombre de alarma:').pack(side=TOP)
    entry_name = Entry(frm_alarm)
    entry_name.pack(side=TOP)

    Label(frm_alarm, text='Hora:').pack(side=TOP)
    entry_hour = Entry(frm_alarm)
    entry_hour.pack(side=TOP)

    Label(frm_alarm, text='Minutos:').pack(side=TOP)
    entry_minute = Entry(frm_alarm)
    entry_minute.pack(side=TOP)

    Label(frm_alarm, text='Segundos:').pack(side=TOP)
    entry_second = Entry(frm_alarm)
    entry_second.pack(side=TOP)

    alarm_sound = IntVar()
    Label(frm_alarm, text='Sonido:').pack(side=TOP)
    rb_seconds = Radiobutton(frm_alarm, text='ringbell',
                             variable=alarm_sound, value=0)
    rb_seconds.pack(side=TOP)
    rb_seconds = Radiobutton(frm_alarm, text='doorbell',
                             variable=alarm_sound, value=1)
    rb_seconds.pack(side=TOP)
    rb_seconds = Radiobutton(
        frm_alarm, text='Forest melody', variable=alarm_sound, value=2)
    rb_seconds.pack(side=TOP)

    Label(frm_alarm, text='Intervalo entre repique de alarma (minutos):').pack(
        side=TOP)
    cmb_interval = Combobox(frm_alarm)
    cmb_interval['values'] = (1, 5, 10, 15, 20)
    cmb_interval.pack(side=TOP)

    Label(frm_alarm, text='Duración de alarma (minutos):').pack(side=TOP)
    cmb_duration = Combobox(frm_alarm)
    cmb_duration['values'] = (5, 10, 20, 30)
    cmb_duration.pack(side=TOP)

    btn_set_alarm.configure(text='Guardar alarma', command=save_alarm)

    frm_alarm.pack()


root = Tk()
root.geometry('400x200')
root.title('Reloj con alarma')

reloj = Clock()

frm_clock = Frame(root)
Label(frm_clock, text=reloj.get_hour()).pack()
btn_set_alarm = Button(frm_clock, text='Establecer alarma', command=set_alarm)
btn_set_alarm.pack()
frm_clock.pack()

root.mainloop()
