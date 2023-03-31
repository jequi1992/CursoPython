print("============================")
print("Programa que indica el clima")
print("============================")
ciudad=input("Ingrese la ciudad: ") # Esta variable guarda el nombre de la ciudad
temp=int(input("Ingrese temperatura: ")) # Esta variable guarda el valor de la temperatura ingresada por el usuario.

if temp<=20:
   print("El clima de "+ciudad+" es frio")
else:
   print("El clima de "+ciudad+" es Caliente")