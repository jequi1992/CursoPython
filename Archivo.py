# print("********************************************")
# print("LISTADO VECINDAD DEL CHAVO")
# print("********************************************")

# with open("C:\\Users\\VIVELAB\\Downloads\\vecindadchavo.csv","r") as archivo:
#     print(archivo.read())

#___________________________________________________________________________________________________________________________________________

while True:
    print()
    print("********************************************")
    print("********  DIRECTORIO PACIENTE      *********")
    print("********  CLINICA MATASANOS        *********")
    print("********************************************")

    print("1. Registrar Paciente \n2. Listar Pacientes \n3. Salir")
    print("--------------------------------------------")

    op=int(input("Ingrese Opción: "))

    if op==1:
        print("********************************************")
        print("********  DIRECTORIO PACIENTE      *********")
        print("********  CLINICA MATASANOS        *********")
        print("********************************************")
        
        numdoc=input("Ingrese el número de documento: ")
        nompac=input("Ingrese el nombre del paciente: ")
        numcon=input("Ingrese el número de contacto: ")
        edadpac=input("Ingrese edad del paciente: ")

        with open("C:\\Users\\VIVELAB\\Downloads\\pacientes.csv","a") as archivo:
            archivo.write('\n'+numdoc+';'+nompac+';'+numcon+';'+edadpac)

    elif op == 2:

        print("********************************************")
        print("********  DIRECTORIO PACIENTE      *********")
        print("********  CLINICA MATASANOS        *********")
        print("********************************************")
        with open("C:\\Users\\VIVELAB\\Downloads\\pacientes.csv","r") as archivo:
            print(archivo.read())

    elif op == 3:

        print("********************************************")
        print("**   SELECCIONO SALIR DEL PROGRAMA        **")
        print("********************************************")
        break
    else:
        print("**   SELECCIONO UNA OPCIÓN VALIDA        **")


    