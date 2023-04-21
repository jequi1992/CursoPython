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


print("*************************")
print("PROGRAMA CREA ARCHIVO TXT")
print("*************************")
lenguajes="Python\nJavascript\nRuby\nPhp\nGo\n"
with open("C:\\Users\\VIVELAB\\Downloads\\Lenguajesprog2.txt","w") as archivo:
    archivo.write(lenguajes)

with open("C:\\Users\\VIVELAB\\Downloads\\Lenguajesprog2.txt","r") as archivo:
    print(archivo.read())
print("-------------------------------------------------------------------")
