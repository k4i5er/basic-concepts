#  ¿Qué es POO (OOP)?
#  - Código para realizar funciones
#  - Trasladar conceptos de la vida cotidiana a programación (abstracción)
#  - Modelado del mundo cotidiano
#  - Objetos (características y funcionalidad)
#    Características: Descripción (son particularidades que describen al objeto)
#    Funcionalidad: Son las acciones que realizar el objeto por sí mismo (con o sin la intervención de factores externos)
#  - Clase: Categorización de objetos
#     Ejemplo: Clase automóvil
#       Características:
#         Tipo de motor
#         Tipo de combustible
#         Marca
#         Potencia
#         Modelo
#         Tipo
#         Capacidad de carga
#         Capacidad de pasajeros
#         Transmisión
#         Palanca
#         Precio
#         Volante
#         Diámetro de rin
#         Tipo de tracción
#         Tipo de frenos
#         Tipo de dirección
#         Condiciones del Chasis
#         Bolsas de aire
#         Capacidad de tanque de combustible
#         Consumo de combustible
#         Pedales
#         Faros
#         Plumas limpia parabrisas
#         Parabrisas
#         Ventanillas
#         Puertas
#         Asientos
#         Cinturones de seguridad
#         Tablero
#         Bocina
#     Funcionalidades:
#         Encender()
#         Apagar()
#         Frenar()
#         Acelerar()
#         Avanzar()
#         Retroceder()
#         Cambiar velocidades()
#         Girar dirección()
#         Encender luces()
#         Apagar luces()
#         Activar limpia parabrisas()
#         Desactivar limpia parabrisas()
#         Activar claxon()
#         Desactivar claxon
#         Subir cristales()
#         Bajar cristales()
#         Activar alarma()
#         Desactivar alarma()
#
# - Herencia:
#     mi_coche = automovil()
#     mi_coche.material_rines = 'aluminio'
#     otro_coche = automovil()
#     root = Tk()
#     root.geometry('100x400')
#     root.mainloop()

# Crear una clase en Python:
class Reloj():
    # Definición de atributos (propiedades)
    numerals = []
    mechanism = ''  # Analógico o digital
    brand = ''
    type_of = ''  # Pulso, escritorio o pared
    bell = False
    led = True
    hour_hand = False
    hours = 0
    minutes = 0
    seconds = 0

    # Definición de métodos
    # Getters (métodos que presentan información del estado de los atributos)
    def get_hour(self):
        print(f'La hora actual es: {self.hours}:{self.minutes}:{self.seconds}')

    def ring_bell(self):
        if(self.bell):
            print('Riiiiiiiiiiing')
        else:
            print('Lo siento joven, pero no le vengo manejando las alarmas )=')

    def backlight_on(self):
        print('Luz encendida')

    def show_clock_items(self):
        numerals = 0
        print(f'''
      Numerales: {self.numerals}
      Tipo de mecanismo: {self.mechanism}
      Marca: {self.brand}
      Tipo de reloj: {self.type_of}
      Campanilla: {self.bell}
      Luz interior: {self.led}
      Manecilla de hora: {self.hour_hand}
      ''')

    # Setters (métodos que modifican atributos)
    def set_hour(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


mi_reloj = Reloj()
mi_reloj.led = True
mi_reloj.mechanism = 'Digital'
mi_reloj.type_of = 'Pulso'
mi_reloj.brand = 'Casio'
mi_reloj.numerals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
mi_reloj.hour_hand = False
mi_reloj.bell = True
mi_reloj.show_clock_items()
mi_reloj.ring_bell()
mi_reloj.set_hour(11, 19, 56)
mi_reloj.get_hour()

otro_reloj = Reloj()
otro_reloj.led = False
otro_reloj.mechanism = 'Analógico'
otro_reloj.type_of = 'Pared'
otro_reloj.brand = 'Acme'
otro_reloj.numerals = ['I', 'II', 'III', 'IV', 'V',
                       'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
otro_reloj.hour_hand = True
otro_reloj.show_clock_items()
otro_reloj.ring_bell()
otro_reloj.get_hour()

# Misión:
# Crear una clase que permita crear relojes con distintos husos horarios para las siguientes
# ciudades:
# Madrid, Tokio, Moscú, Centro de la CDMX, Nueva York
# y que permita visualizar la hora actual CORRECTA de las distintas ciudades
# hora_madrid = Reloj()
# hora_madrid.set_city('Madrid')
# hora_madrid.get_hour()  # La hora en Madrid es: 18:31:55
