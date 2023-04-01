from tkinter import *
from tkinter import filedialog
from colorama import Fore
from XML import XML
#import os
#import webbrowser


class Main:

    def __init__(self):
        self.ruta = ''  # -----> Guarda la dirección del archivo XML
        self.op = ''  # -----> Guarda la opción seleccionada del menú
        self.compuesto_seleccionado = False  # -----> variable para seleccionar un compuesto
        self.maquina_seleccionada = False  # -----> variable para seleccionar una maquina
        self.salir = False  # -----> Variable para finalizar el programa
        self.archivo = XML()

    def menu_principal(self):  # -----> Metodo para mostrar el menu principal
        while not self.salir:  # -----> Mientras self.salir sea = False...
            print('                                                       ')
            print(Fore.GREEN + '┌----------- MENU PRINCIPAL -------------┐')
            print(Fore.GREEN + '|                                        |')
            print(Fore.GREEN + '|       1)   Reiniciar sistema           |')
            print(Fore.GREEN + '|       2)   Cargar archivo              |')
            print(Fore.GREEN + '|       3)   Gestion de elementos        |')
            print(Fore.GREEN + '|       4)   Gestion de maquinas         |')
            print(Fore.GREEN + '|       5)   Gestion de compuestos       |')
            print(Fore.GREEN + '|       6)   Generar XML                 |')
            print(Fore.GREEN + '|       7)   Ayuda                       |')
            print(Fore.GREEN + '|       8)   Finalizar programa          |')
            print(Fore.GREEN + '|                                        |')
            print(Fore.GREEN + '└----------------------------------------┘')
            print('                                                       ')

            self.op = input(Fore.CYAN + '--> Ingrese una opción: ')

            if self.op == '1':
                self.reiniciar_sistema()
            elif self.op == '2':
                self.cargar_archivo()
            elif self.op == '3':
                self.gestionar_elementos()
            elif self.op == '4':
                self.gestionar_maquinas()
            elif self.op == '5':
                self.gestionar_compuestos()
            elif self.op == '6':
                self.generar_xml()
            elif self.op == '7':
                self.ayuda()
            elif self.op == '8':
                self.finalizar()
            else:
                print('                               ')
                print(Fore.RED + '--> Opción no valida')

    def reiniciar_sistema(self):  # -----> Metodo para reiniciar la memoria del programa
        pass

    def cargar_archivo(self):  # -----> Metodo para cargar archivos XML
        ventana = Tk()
        respaldo = self.ruta
        self.ruta = ''

        self.ruta = filedialog.askopenfilename(
            title='Buscar archivo',
            filetypes=[
                ('Archivos xml', '*.xml'),
                ('Todos los archivos', '*.*')
            ]
        )
        if self.ruta == '':
            self.ruta = respaldo
            print('                                         ')
            print(Fore.RED + '--> No se cargo ningun archivo')
        else:
            self.archivo.leer_xml(self.ruta)
            print('                                         ')
            print(Fore.CYAN + '--> Archivo cargado con exito')
        ventana.mainloop()

    def gestionar_elementos(self):
        pass

    def gestionar_maquinas(self):
        pass

    def gestionar_compuestos(self):
        pass

    def generar_xml(self):
        pass

    def ayuda(self):
        pass

    def finalizar(self):  # -----> Metodo para finalizar el programa
        print('                                  ')
        print(Fore.RED + '--> Programa finalizado')
        self.ruta = ''
        self.op = ''
        self.compuesto_seleccionado = False
        self.maquina_seleccionada = False
        self.salir = True


app = Main()
app.menu_principal()
