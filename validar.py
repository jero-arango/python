#Nombre del archivo: validar.py
#Autor: Jeronimo Arango Rendon
#fecha: 18/03/23
#=======================================================================================================================================
while True:
    menu = """
    Bienvenidos al registro de usuarios, llene los campos que le soliciten y seleccione un numero del 1 al 4
    [1]Digitar su nombre
    [2]Digitar su edad
    [3]Digitar su email
    [4]Salir del programa
    """
    print(menu)
    opcion=input('entre la opcion 1, 2, 3 o 4: ')
    if opcion=='1':
        while True:
            nombre = input('digite su nombre: ')
            if nombre.isalpha():
                print("su nombre es: ",nombre)
                break
            else:
                print('su nombre esta mal digitado')

    elif opcion=='2':
        while True:
            edad = input('digite su edad: ')
            if edad.isnumeric():
                print("su edad es: ",edad)
                break
            else:
                print('su edad esta mal digitado')

    elif opcion=='3':
        while True:
            email = input('digite su email: ')
            if email.find('@') >=1 and email.find('.')>=0:
                print("su email es: ",email)
                break
            else:
                print('su email esta mal digitado')

    elif opcion == '4':
        exit()

