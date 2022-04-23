Primero definimos variables entre ellas montos, salir y saldo. 
from tkinter import Menu
montos = [20, 50, 100, 150, 500]
salir = True
saldo = 10000

Luego definiremos las funciones menú, retiro, ver saldo y salir.
En cuanto la función retiro lo que se hace primero es globalizar el saldo para que sea el mismo tanto como para retiro y para ver saldo, luego se imprime escoge tu monto y las cantidades de monto a retirar para que 
el usuario pueda escoger, op1 será igual a la cantidad a dinero a retirar que nosotros digitemos si retirar es igual a 0:
    if retirar ==0:
        print("Sólo puede escoger uno de los montos propuestos.")
        input("Pulse Enter para volver al menú.")

Si retirar es mayor al saldo:
    elif retirar > saldo:
        print("No tiene el saldo suficiente para este retiro.")
        input("Pulse Enter para volver al menú.")

Ahora para poder restar el saldo con la cantidad a retirar se ejecuta for i en montos para que busque por caca uno de los elementos que contiene la lista montos y así se pueda retirar el dinero en la lista.
Si la variable retirar es igual a i el saldo se resta con el monto a retirar y ese será el nuevo valor de saldo, una vez realizado el retito se imprimirá el dinero en la cuenta más el saldo restante, nos saldrá un 
input que diga pulse enter para volver a la acción.
    for i in montos:
        if retirar ==i:
            saldo-=retirar
            print(f"Dinero en la cuenta: {saldo}.")
            input("Pulse Enter para volver al menú.")

La función ver saldo lo único que hacemos es imprimir un string la cual diga dinero en la cuenta más la variable saldo.
def versaldo():
    print(f"Dinero en la cuenta: {saldo}.")

Finalmente, para la función salir se imprime gracias por utilizar el cajero automático y si la variable salir se igual false el código rompe.
def Salir():
    print("Gracias por utilizar el cajero automático.")
    while salir ==False:
        break

Al iniciar el código nos imprimirá bienvenido al cajero automático luego nos pedirá ingresar la contraseña la cual esta es diferente de 1313 nos saldrá un input la cual diga contraseña incorrecta inténtelo de nuevo y 
si esta es correcta nos enviara al menú.
print("Bienvenido al cajero automático.")
contra = input("Ingrese la contraseña: ")
while contra != "1313":
    contra = input("Contraseña incorrecta, inténtelo de nuevo: ")
else:
    MENU()

Para finalizar con la función menú nos imprimirá menú luego las opciones del cajero, si la variable opción es igual a 1 nos ejecutara la función de retiro, si la variable opción es 2 nos ejecutara la función ver saldo y 
si la opción variable es 3 nos ejecutara salir, al finalizar la función y ver saldo siempre regresaremos al menú.
def MENU():
    print("\t.:MENU:")
    print("1. Retirar dinero en la cuenta")
    print("2. Mostrar dinero disponible")
    print("3. Salir")
    opcion = int(input("Digite una opción del menú: "))
    if opcion ==1:
        retiro()
        MENU()
    if opcion ==2:
        versaldo()
        input("Pulse Enter para volver al menú.")
        MENU()
    if opcion ==3:
        Salir()
        salir=False
