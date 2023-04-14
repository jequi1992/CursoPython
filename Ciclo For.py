print("============================")
print("       USO DEL FOR          ")
print("============================")
numeros=[5,8,7,9,12,2,3] # En esta variable se almacena la lista de items que componen el conjunto.
for i in numeros: # En esta linea se recorre la lista segun la iteracción de la variable i
  print(i)
print("============================") 
#-------------------------------------------------------------------------------------------------------#
print("**** INICIAR *****")
for elemento in [0,1,10,3,8]: # En esta linea se recorre la lista segun la iteracción de la variable i
  print(elemento,end=",") # En esta linea se imprime la lista de items en una misma linea separada por comas
print()
print("fin del For") 
#-------------------------------------------------------------------------------------------------------#
print("**** INICIAR *****")
for i in [0,1,10,3,8]: # En esta linea se recorre la lista segun la iteracción de la variable i
  print("SENA ",",","ESPINAL") # En esta linea se imprime la lista de items en una misma linea separada por comas
print()
print("fin del For") 
#-------------------------------------------------------------------------------------------------------#
print("**** INICIAR *****")
for i in [0,1,10,3,8]: # En esta linea se recorre la lista segun la iteracción de la variable i
  print("SENA","-","ESPINAL", end=",") # En esta linea se imprime la lista de items en una misma linea separada por comas
print()
print("fin del For") 
#-------------------------------------------------------------------------------------------------------#
print("**** INICIAR *****")
for i in ["LUNES","MARTES","MIERCOLES","JUEVES","VIERNES","SABADO","DOMINGO"]: # En esta linea se recorre la lista segun la iteracción de la variable i
  print(i) # En esta linea se imprime la lista de items en una misma linea separada por comas
print()
print("fin del For") 
#-------------------------------------------------------------------------------------------------------#
print("============================")
print("  USO DEL FOR CON RANGE     ")
print("============================")
ini=int(input("Numero Inicia: "))
fin=int(input("Numero Finaliza: "))
print("============================")
for i in range(ini,fin,2): # En esta linea se recorre la lista segun la iteracción de la variable i
  print(i,",",end="") # En esta linea se imprime la lista de items en una misma linea separada por comas
print()
print("fin del For") 
#-------------------------------------------------------------------------------------------------------#
print("============================")
print("  USO DEL FOR CON RANGE     ")
print("============================")
for i in range(5): # En esta linea se recorre la lista segun la iteracción de la variable i
  print(i,",",end="") # En esta linea se imprime la lista de items en una misma linea separada por comas
print()
print("fin del For") 
#-------------------------------------------------------------------------------------------------------#
print("============================")
print("  USO DEL FOR CON RANGE     ")
print("============================")
for i in range(10,15): # En esta linea se recorre la lista segun la iteracción de la variable i
  print(i,",",end="") # En esta linea se imprime la lista de items en una misma linea separada por comas
print()
print("fin del For") 

#-------------------------------------------------------------------------------------------------------#
#Programa que imprime tablas de multiplicar

print("=================================")
print("GENERACIÓN TABALAS DE MULTIPLICAR")
print("=================================")

n = int(input("Ingrese la tabla de multiplicar"))
print("=====================================")
print("TABLA MULTIPLICAR DEL ---->: ",n)
for i in range(1,11):
  print(n,"*",i,"=",i*n)

#-------------------------------------------------------------------------------------------------------#

#Realizar un programa que pregunte por teclado una frase o una oración y que indique mediante un mensaje decir cuantas vocales hay

print("========================================")
print("PROGRAMA QUE CUENTA VOCALES EN UNA FRASE")
print("========================================")

frase = input("Ingrese Frase: ")
vocales ="aeiouAEIOU"

#Se define un contador de vocales

cuentavocal=0
for i in frase:

  # Examinar si el caracter validado es una vocal

  if i in vocales:
    cuentavocal=cuentavocal+1
print()
print("El numero de vocales en la frase es: ", cuentavocal)

#-------------------------------------------------------------------------------------------------------#

#programa que me diga cuantas notas quiere promediar y luego que me pregunte el nombre del estudiante, 
#asignatura y la nota y luego diga el promedio del curso

print("=============================================")
print("PROGRAMA QUE CUENTA CALCULA LA NOTA DEL CURSO")
print("=============================================")

acumulador=0
nombre = input("Nombre del Estudiante: ")
asignaturas = int(input("Ingrese la cantidad de asignaturas a promediar: "))
print()
for i in range(asignaturas):
  materia=input("Nombre de la asignatura: ")
  nota=float(input("Ingrese la nota de "+materia+": "))
  acumulador=acumulador+nota
  print()

print("El promedio del curso es: ", round((acumulador/asignaturas),2))

#-------------------------------------------------------------------------------------------------------#

print("============================================================")
print("PROGRAMA QUE CUENTA VOCALES ABIERTAS Y CERRADAS EN UNA FRASE")
print("============================================================")

frase = input("Ingrese Frase: ")
vocales_abiertas ="aeoAEO"
vocales_cerradas ="iuIU"

#Se define un contador de vocales

cuentavocalabiertas=0
cuentavocalcerradas=0

for i in frase:

  # Examinar si el caracter validado es una vocal

  if i in vocales_abiertas:
    cuentavocalabiertas=cuentavocalabiertas+1
  elif i in vocales_cerradas:
    cuentavocalcerradas=cuentavocalcerradas+1
print()
print("El numero de vocales abiertas en la frase es: ", cuentavocalabiertas)
print("El numero de vocales cerradas en la frase es: ", cuentavocalcerradas)

#-------------------------------------------------------------------------------------------------------#

print("============================================")
print("*****VENTA DE ARTICULOS - LA TUMBADORA******")
print("============================================")

numproductos = int(input("Ingrese el numero de articulos a Comprar: "))

# Se define un contador de articulos, acumulador de valor productos

contador=0
sumaproducto=0

for i in range(numproductos):
  print("DATOS PRODUCTO")
  producto = input("Ingrese el producto: ")
  precio = float(input("Ingrese el precio: "))
  cantidad = int(input("Ingrese la cantidad: "))
  valorproducto=precio*cantidad
  sumaproducto=sumaproducto+valorproducto
  print()

IVA=0.19*sumaproducto
valorfactura=sumaproducto+IVA
print()
print("El valor del IVA es: ", IVA)
print("El valor a pagar es: ", valorfactura)

#-------------------------------------------------------------------------------------------------------#

import random

print("=========================================")
print("*****SIMULA LANZAMIENTOS DE UN DADO******")
print("=========================================")

lanzamiento=int(input("Indique el numero de lanzamiento ----> "))
totpuntos=0
for i in range(lanzamiento):
  dado=random.randrange(1,7)
  print(f"Lanzamiento {i+1} : {dado}")
  totpuntos +=dado
print(f"En total ha obtenido {totpuntos} punto(s)")
print("=========================================")
