from cola import Cola
from colaEnlazada import ColaE

if __name__ == "__main__":
    opcion = 0
    while opcion != "3":
        print("\n1. Ingresar una cola secuencial")
        print("2. Ingresar una cola enlazada")
        print("3. Salir")
        opcion = input("Ingrese la opcion a realizar:")

        if opcion == "1":
            cant = int(input("\nIngrese la cantidad de componentes:"))
            unaCola = Cola(cant)
            for i in range(cant):
                x = input("Ingrese el dato:")
                unaCola.insertar(x)
            print("\nMostra los elementos de la cola")
            unaCola.mostrar()
            print("\nSuprimiendo un elemento...")
            unaCola.suprimir()
            print("\nMostra los elementos de la cola suprimiendo el primer")
            unaCola.mostrar()

        if opcion == "2":
            cant = int(input("\nIngrese la cantidad de componentes:"))
            unaCola = ColaE(cant)
            for i in range(cant):
                x = input("Ingrese el elemento a ingresar:")
                unaCola.insertar(x)
            print("\nMostra los elementos de la cola")
            unaCola.mostrar()
            print("\nSuprimiendo un elemento...")
            print("El elemento suprimido es:{}".format(unaCola.suprimir()))
            print("\nMostra los elementos de la cola suprimiendo el primero")
            unaCola.mostrar()