# print("*******************************************")
# print("PROGRAMA QUE ABRE, LEE, IMPRIME ARCHIVO TXT")
# print("*******************************************")
# # archivo=open("C:\\Users\\VIVELAB\\Downloads\\chavo.txt") # Con esta forma se puede abrir archivo tambien
# with open("C:\\Users\\VIVELAB\\Downloads\\chavo.txt","r") as archivo:
#     # print(archivo.read()) # Con esta linea de codigo trae todo el contenido del archivo
#     # print(archivo.readline()) # Con esta linea de codigo trae solo la primera linea
#     print(archivo.readlines()) # Con esta linea de codigo trae todas las lineas de un archivo separado por comas.

# print("-------------------------------------------------------------------")
# # archivo.close()

# # _______________________________________________________________________________________________________________________

# print("*******************************************")
# print("PROGRAMA QUE ABRE, LEE, IMPRIME ARCHIVO TXT")
# print("*******************************************")
# archivo=open("C:\\Users\\VIVELAB\\Downloads\\chavo - copia.txt")
# # archivo=open("C:\\Users\\VIVELAB\\Downloads\\chavo.txt") # Con esta forma se puede abrir archivo tambien
# with open("C:\\Users\\VIVELAB\\Downloads\\chavo.txt","w") as archivo:
#     archivo.write("Paty es Bonita y coqueta")
#     archivo.write("Florinda le Pega a Don Ramon")
#     print("Lineas agregadas al archivo txt")
# print("-------------------------------------------------------------------")

# # # _______________________________________________________________________________________________________________________


# print("*******************************************")
# print("PROGRAMA QUE ABRE, LEE, IMPRIME ARCHIVO TXT")
# print("*******************************************")
# with open("C:\\Users\\VIVELAB\\Downloads\\chavo.txt","a") as archivo:
#     archivo.write("\n8. Paty es Bonita y coqueta\n")
#     archivo.write("9. Florinda le Pega a Don Ramon\n")

# with open("C:\\Users\\VIVELAB\\Downloads\\chavo.txt","r") as archivo:
#     print(archivo.read())
# print("-------------------------------------------------------------------")


# # # _______________________________________________________________________________________________________________________


# print("*************************")
# print("PROGRAMA CREA ARCHIVO TXT")
# print("*************************")
# lenguajes="Python\nJavascript\nRuby\nPhp\nGo\n"
# with open("C:\\Users\\VIVELAB\\Downloads\\Lenguajesprog2.txt","w") as archivo:
#     archivo.write(lenguajes)

# with open("C:\\Users\\VIVELAB\\Downloads\\Lenguajesprog2.txt","r") as archivo:
#     print(archivo.read())
# print("-------------------------------------------------------------------")


 # _______________________________________________________________________________________________________________________

# print("*************************")
# print("PROGRAMA CREA ARCHIVO TXT")
# print("*************************")
# from shutil import copyfile
# copyfile("C:\\Users\\VIVELAB\\Downloads\\Lenguajesprog1.txt", "C:\\Users\\VIVELAB\\Downloads\\Lenguajesprog3.txt")
# lenguajes="Python\nJavascript\nRuby\nPhp\nGo\n"

# with open("C:\\Users\\VIVELAB\\Downloads\\Lenguajesprog3.txt","r") as archivo:
#     print(archivo.read())
# print("-------------------------------------------------------------------")

#  # _______________________________________________________________________________________________________________________

print("*********************************")
print("LEE ARCHIVO TXT Y PROMEDIA EDADES")
print("*********************************")

sumaedad=0
cuentaedades=0

with open("C:\\Users\\VIVELAB\\Downloads\\edades.txt","r") as archivo:
    for edad in archivo:
        sumaedad+=int(edad)
        cuentaedades +=1

promedad=round(sumaedad/cuentaedades,2)

print("El promedio de edades es de ---->", promedad)
print("La sumatoria de las edades es de ---->", sumaedad)
print("El numero de edades promediadas es de ---->", cuentaedades)

# _______________________________________________________________________________________________________________________

print("*********************************")
print("LEE ARCHIVO TXT, TOTALIZA, MAXIMO VALOR - DEUDA")
print("*********************************")

sumadeuda=0
max=0

with open("C:\\Users\\VIVELAB\\Downloads\\deudas.txt","r") as archivo:
    for deuda in archivo:
        sumadeuda+=int(deuda)
        if max>int(deuda):
            may=max
        else:
            may=int(deuda)
        max=may

promedad=round(sumaedad/cuentaedades,2)

print("===========================================")
print("El valor de la Deuda es de ---->", sumadeuda)
print("El valor maximo es ---->", max)
print("===========================================")

# _______________________________________________________________________________________________________________________

print("********************************************")
print("LEE ARCHIVO TXT ADICIONA 3 FILAS - VEHICULOS")
print("********************************************")

with open("C:\\Users\\VIVELAB\\Downloads\\vehiculos.txt","a") as archivo:
    archivo.write("\nFGY458 CAMIONETA KIA 2021 PANCRACIO PATAQUIVA\n")
    archivo.write("ZGT159 AUTOMOVIL TOYOTA 2023 ANASTACIA CIPAGAUTA\n")
    archivo.write("UGN400 CAMIONETA MAZDA 2015 SIGIFREDO TUTA\n")

print("============================")
print("FILAS AGREGADAS EXITOSAMENTE")
print("============================")


with open("C:\\Users\\VIVELAB\\Downloads\\vehiculos.txt","r") as archivo:
    print(archivo.read())

# _______________________________________________________________________________________________________________________

import os

print("********************************************")
print("ELIMINA UN ARCHIVO TXT")
print("********************************************")

os.remove("C:\\Users\\VIVELAB\\Downloads\\tirra.jpg")

print("============================")
print("FILAS AGREGADAS EXITOSAMENTE")
print("============================")
