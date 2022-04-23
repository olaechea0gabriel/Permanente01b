from tkinter import Menu
montos = [20, 50, 100, 150, 500]
salir = True
saldo = 10000
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

def retiro():
    global saldo
    print("\t.:Escoge tu monto:")
    print("1. S/20")
    print("2. S/50")
    print("3. S/100")
    print("4. S/150")
    print("5. S/500")
    op1 = int(input("Dinero a retirar: "))
    retirar = int(op1)
    if retirar ==0:
        print("Sólo puede escoger uno de los montos propuestos.")
        input("Pulse Enter para volver al menú.")
    elif retirar > saldo:
        print("No tiene el saldo suficiente para este retiro.")
        input("Pulse Enter para volver al menú.")
    for i in montos:
        if retirar ==i:
            saldo-=retirar
            print(f"Dinero en la cuenta: {saldo}.")
            input("Pulse Enter para volver al menú.")
        
    
def versaldo():
    print(f"Dinero en la cuenta: {saldo}.")
    
def Salir():
    print("Gracias por utilizar el cajero automático.")
    while salir ==False:
        break

print("Bienvenido al cajero automático.")
contra = input("Ingrese la contraseña: ")
while contra != "1313":
    contra = input("Contraseña incorrecta, inténtelo de nuevo: ")
else:
    MENU()