import math
from os import system
class Triangulo:
    def __init__(self,lado1,lado2,lado3,tipo):
        self.__lado1=lado1
        self.__lado2=lado2
        self.__lado3=lado3
        self.__tipo=tipo
    @property
    def lado1(self):
        return self.__lado1
    @property
    def lado2(self):
        return self.__lado2
    @property
    def lado3(self):
        return self.__lado3
    @property
    def tipo(self):
        return self.__tipo
    def PerimetroTriangulo(self):
         return self.__lado1+self.__lado2+self.__lado3

         
    def AreaTriangulo(self):
        s= self.__lado1+self.__lado2+self.__lado3 / 2
        area = math.sqrt(s-self.__lado1)+(s-self.__lado2)+(s-self.__lado3)/2
        return area
    
    def __add__(self,otro):
        return self.__AreaTriangulo()+otro.AreaTriangulo()
    
ListaTriangulos= []
none=[]
SEPARADOR=("*" * 40 + "\n")
while True:
    opcion = int(input( " ***Bienvenido al menu***\n 1.-Registrar un nuevo triangulo\n 2.-Mostrar la informacion de cada triangulo\n 3.-Salir\n Opcion:"))
    print(SEPARADOR)
    
    if opcion==1:
        L1 = int(input("Lado1: "))
        L2 = int(input("Lado2: "))
        L3 = int(input("Lado3: "))
        if L1 == L2 and L1 == L3 or L2 == L3:
            TrianguloIndefinido=Triangulo(L1,L2,L3,"El triangulo es: Equilatero")
            ListaTriangulos.append(TrianguloIndefinido)
        elif L1 == L2 or L1 == L3 or L2 == L3:
            TrianguloIndefinido = Triangulo(L1,L2,L3, "El triangulo es: Isosceles")
            ListaTriangulos.append(TrianguloIndefinido)
        else:
            TrianguloIndefinido = Triangulo(L1,L2,L3, "El triangulo es: Escaleno")
            ListaTriangulos.append(TrianguloIndefinido)
            system("cls")
        print(SEPARADOR)
    elif opcion == 2:
        if ListaTriangulos==none:
            print ("No hay ningun triangulo registrado, registre uno por favor")
            print(SEPARADOR)
        else:
            for triangulo in ListaTriangulos:
                area=triangulo.AreaTriangulo()
                print(f"Esta es el area del triangulo {area}")
                perimetro=triangulo.PerimetroTriangulo()
                print(f"Este es el perimetro {perimetro}")
                print(triangulo.tipo)
                suma=0
            for triangulo in ListaTriangulos:
                suma += triangulo.AreaTriangulo()
           
            print(SEPARADOR)
    elif opcion == 3:
        break