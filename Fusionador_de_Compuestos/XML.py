from xml.dom import minidom
from colorama import Fore
from TDA import SCList
#  from Graphics import Graphics
#  from Operations import Operations


class XML:

    def __init__(self):
        self.ruta_xml = ''  # -----> Guarda la dirección del archivo XML
        self.lista_nombres_elementos = SCList()  # -----> Lista con los nombres de los elementos
        self.lista_nombres_maquinas = SCList()  # -----> Lista con los nombres de las maquinas
        self.lista_nombres_compuestos = SCList()  # -----> Lista con los nombres de los compuestos
        self.lista_elementos = SCList()  # -----> Lista con todos los elementos (posición, elemento)
        self.lista_maquinas = SCList()  # -----> Lista con todas las maquinas (posición, maquina)
        self.lista_compuestos = SCList()  # -----> Lista con todos los compuestos (posición, compuesto)
        self.elemento = []  # -----> Contiene toda la información de 1 elemento
        self.maquina = []  # -----> Contiene toda la información de 1 maquina
        self.compuesto = []  # -----> Contiene toda la información de 1 compuesto
        self.lista_pines = []  # -----> Es una lista con todos los pines
        self.pin = []  # -----> Contiene la información de 1 pin
        self.formula = []  # -----> Contiene los elementos de 1 compuesto
        self.numeros = []  # -----> Lista con los numeros atomicos de los elementos
        self.simbolos = []  # -----> Lista con los simbolos de los elementos
        self.nombres = []  # -----> Lista con los nombres de los elementos
        self.contador_1 = 1  # -----> Contador de elementos
        self.contador_2 = 1  # -----> Contador de maquinas
        self.contador_3 = 1  # -----> Contador de compuestos

    def leer_xml(self, ruta):
        self.ruta_xml = ruta
        xml = minidom.parse(self.ruta_xml)
        elementos = xml.getElementsByTagName('listaElementos')
        maquinas = xml.getElementsByTagName('Maquina')
        compuestos = xml.getElementsByTagName('compuesto')

        for elemento in elementos:
            lista_elementos = elemento.getElementsByTagName('elemento')

            for dato in lista_elementos:
                numero = dato.getElementsByTagName('numeroAtomico')[0]
                simbolo = dato.getElementsByTagName('simbolo')[0]
                nombre = dato.getElementsByTagName('nombreElemento')[0]

                self.lista_nombres_elementos.agregar_fin(f'{self.contador_1}) {nombre.firstChild.data}')
                self.elemento.append(numero.firstChild.data)
                self.numeros.append(numero.firstChild.data)
                self.elemento.append(simbolo.firstChild.data)
                self.simbolos.append(simbolo.firstChild.data)
                self.elemento.append(nombre.firstChild.data)
                self.nombres.append(nombre.firstChild.data)
                self.lista_elementos.agregar_fin(str(self.contador_1))
                self.lista_elementos.agregar_fin(self.elemento)
                self.elemento = []
                self.contador_1 = self.contador_1 + 1

        for maquina in maquinas:
            nombre = maquina.getElementsByTagName('nombre')[0]
            numero_pines = maquina.getElementsByTagName('numeroPines')[0]
            numero_elementos = maquina.getElementsByTagName('numeroElementos')[0]
            lista_pines = maquina.getElementsByTagName('pin')

            self.lista_nombres_maquinas.agregar_fin(f'{self.contador_2}) {nombre.firstChild.data}')
            self.maquina.append(nombre.firstChild.data)
            self.maquina.append(numero_pines.firstChild.data)
            self.maquina.append(numero_elementos.firstChild.data)

            for pin in lista_pines:
                lista_elementos = pin.getElementsByTagName('elemento')

                for elemento in lista_elementos:
                    self.pin.append(elemento.firstChild.data)

                self.lista_pines.append(self.pin)
                self.pin = []

            self.maquina.append(self.lista_pines)
            self.lista_pines = []
            self.lista_maquinas.agregar_fin(str(self.contador_2))
            self.lista_maquinas.agregar_fin(self.maquina)
            self.maquina = []
            self.contador_2 = self.contador_2 + 1

        for compuesto in compuestos:
            nombre = compuesto.getElementsByTagName('nombre')[0]
            lista_elementos = compuesto.getElementsByTagName('elemento')

            for elemento in lista_elementos:
                self.formula.append(elemento.firstChild.data)

            self.lista_nombres_compuestos.agregar_fin(f'{self.contador_3}) {nombre.firstChild.data}: {self.formula}')
            self.compuesto.append(nombre.firstChild.data)
            self.compuesto.append(self.formula)
            self.formula = []
            self.lista_compuestos.agregar_fin(str(self.contador_3))
            self.lista_compuestos.agregar_fin(self.compuesto)
            self.compuesto = []
            self.contador_3 = self.contador_3 + 1

    def mostrar_elementos(self):
        print('                                                ')
        print(Fore.GREEN + '--> Lista de elementos disponibles:')
        print('                                                ')
        self.lista_nombres_elementos.mostrar_contenido()

    def agregar_elementos(self):
        print('                                                    ')
        numero = input(Fore.CYAN + '--> Ingrese el número atomico: ')

        if numero in self.numeros:
            print('                                                                  ')
            print(Fore.RED + '--> Ya existe otro elemento con el mismo número atomico')
        else:
            print('                                              ')
            simbolo = input(Fore.CYAN + '--> Ingrese el simbolo: ')

            if simbolo in self.simbolos:
                print('                                                           ')
                print(Fore.RED + '--> Ya existe otro elemento con el mismo simbolo')
            else:
                print('                                            ')
                nombre = input(Fore.CYAN + '--> Ingrese el nombre: ')

                if nombre in self.nombres:
                    print('                                                          ')
                    print(Fore.RED + '--> Ya existe otro elemento con el mismo nombre')
                else:
                    self.lista_nombres_elementos.agregar_fin(f'{self.contador_1}) {nombre}')
                    self.elemento.append(numero)
                    self.numeros.append(numero)
                    self.elemento.append(simbolo)
                    self.simbolos.append(simbolo)
                    self.elemento.append(nombre)
                    self.nombres.append(nombre)
                    self.lista_elementos.agregar_fin(str(self.contador_1))
                    self.lista_elementos.agregar_fin(self.elemento)
                    self.elemento = []
                    self.contador_1 = self.contador_1 + 1
                    print('                                               ')
                    print(Fore.CYAN + '--> Nuevo elemento químico agregado')

    def mostrar_maquinas(self):
        print('                                               ')
        print(Fore.GREEN + '--> Lista de maquinas disponibles:')
        print('                                               ')
        self.lista_nombres_maquinas.mostrar_contenido()

    def seleccionar_maquina(self):
        print('                                               ')
        print(Fore.GREEN + '--> Lista de maquinas disponibles:')
        print('                                               ')
        self.lista_nombres_maquinas.mostrar_contenido()
        print('                                                   ')
        posicion = input(Fore.CYAN + '--> Seleccione una maquina: ')
        maquina = self.lista_maquinas.buscar(posicion)
        if maquina is not None:
            return maquina

    def mostrar_compuestos(self):
        print('                                                 ')
        print(Fore.GREEN + '--> Lista de compuestos disponibles:')
        print('                                                 ')
        self.lista_nombres_compuestos.mostrar_contenido()

    def seleccionar_compuesto(self):
        print('                                                 ')
        print(Fore.GREEN + '--> Lista de compuestos disponibles:')
        print('                                                 ')
        self.lista_nombres_compuestos.mostrar_contenido()
        print('                                                    ')
        posicion = input(Fore.CYAN + '--> Seleccione un compuesto: ')
        compuesto = self.lista_compuestos.buscar(posicion)
        if compuesto is not None:
            return compuesto
