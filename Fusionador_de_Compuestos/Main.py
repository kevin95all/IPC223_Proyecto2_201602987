from tkinter import *
from tkinter import filedialog
from colorama import Fore
from XML import XML
#  import os
#  import webbrowser


class Main:

    def __init__(self):
        self.ruta = ''  # -----> Guarda la dirección del archivo XML
        self.op = ''  # -----> Guarda la opción seleccionada del menú
        self.compuesto_analizado = False  # -----> Variable para analizar el compuesto
        self.salir = False  # -----> Variable para finalizar el programa
        self.archivo = XML()

    def menu_principal(self):  # -----> Metodo para mostrar el menu principal
        while not self.salir:  # -----> Mientras self.salir sea = False...
            print('                                                       ')
            print(Fore.GREEN + '┌----------- MENU PRINCIPAL -------------┐')
            print(Fore.GREEN + '|                                        |')
            print(Fore.GREEN + '|       1)   Reiniciar sistema           |')
            print(Fore.GREEN + '|       2)   Cargar archivo              |')
            print(Fore.GREEN + '|       3)   Gestión de elementos        |')
            print(Fore.GREEN + '|       4)   Gestión de maquinas         |')
            print(Fore.GREEN + '|       5)   Gestión de compuestos       |')
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
        if self.ruta == '':
            print('                                              ')
            print(Fore.RED + '--> No se ha cargado ningun archivo')
        else:
            salir = False

            while not salir:
                print('                                                     ')
                print(Fore.GREEN + '┌---------Gestión de elementos---------┐')
                print(Fore.GREEN + '|                                      |')
                print(Fore.GREEN + '|        1)   Mostrar elementos        |')
                print(Fore.GREEN + '|        2)   Agregar elemento         |')
                print(Fore.GREEN + '|        3)   Finalizar                |')
                print(Fore.GREEN + '|                                      |')
                print(Fore.GREEN + '└--------------------------------------┘')
                print('                                                     ')

                op = input(Fore.CYAN + '--> Ingrese una opción: ')

                if op == '1':
                    self.archivo.mostrar_elementos()
                elif op == '2':
                    self.archivo.agregar_elementos()
                elif op == '3':
                    salir = True
                else:
                    print('                               ')
                    print(Fore.RED + '--> Opción no valida')

    def gestionar_maquinas(self):
        if self.ruta == '':
            print('                                              ')
            print(Fore.RED + '--> No se ha cargado ningun archivo')
        else:
            salir = False

            while not salir:
                print('                                                     ')
                print(Fore.GREEN + '┌----------Gestión de máquinas---------┐')
                print(Fore.GREEN + '|                                      |')
                print(Fore.GREEN + '|        1)   Mostrar máquinas         |')
                print(Fore.GREEN + '|        2)   Finalizar                |')
                print(Fore.GREEN + '|                                      |')
                print(Fore.GREEN + '└--------------------------------------┘')
                print('                                                     ')

                op = input(Fore.CYAN + '--> Ingrese una opción: ')

                if op == '1':
                    self.archivo.mostrar_maquinas()
                elif op == '2':
                    salir = True
                else:
                    print('                               ')
                    print(Fore.RED + '--> Opción no valida')

    def gestionar_compuestos(self):
        if self.ruta == '':
            print('                                              ')
            print(Fore.RED + '--> No se ha cargado ningun archivo')
        else:
            salir = False

            while not salir:
                print('                                                     ')
                print(Fore.GREEN + '┌---------Gestión de compuesto---------┐')
                print(Fore.GREEN + '|                                      |')
                print(Fore.GREEN + '|        1)   Mostrar compuestos       |')
                print(Fore.GREEN + '|        2)   Analizar compuesto       |')
                print(Fore.GREEN + '|        3)   Finalizar                |')
                print(Fore.GREEN + '|                                      |')
                print(Fore.GREEN + '└--------------------------------------┘')
                print('                                                     ')

                op = input(Fore.CYAN + '--> Ingrese una opción: ')

                if op == '1':
                    self.archivo.mostrar_compuestos()
                elif op == '2':
                    compuesto = self.archivo.seleccionar_compuesto()
                    maquina = self.archivo.seleccionar_maquina()
                    self.compuesto_analizado = True
                elif op == '3':
                    salir = True
                else:
                    print('                               ')
                    print(Fore.RED + '--> Opción no valida')

    def generar_xml(self):
        pass

    def ayuda(self):
        pass

    def finalizar(self):  # -----> Metodo para finalizar el programa
        print('                                  ')
        print(Fore.RED + '--> Programa finalizado')
        self.ruta = ''
        self.op = ''
        self.compuesto_analizado = False
        self.salir = True


app = Main()
app.menu_principal()
