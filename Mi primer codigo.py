print("=====================")
print("Area de un circulo")
print("=====================")
pi=3.1416 # Este valor corresponde a la constante del valor de PI
nombre=input("Ingrese su nombre: ") # Esta variable guarda el nombre del Usuario
radio=float(input("Ingrese el radio: ")) # Esta variable guarda el valor de radio ingresado por el usuario.
area =round(pi*(radio**2),2) # En esta variable se almancena el resultado de la formula para hallar el area de la circunferencia
str(area) # Se hace la conversiòn de la variable numerica a Cadena de texto
print(nombre+" "+" el area es =", area) #Se muestra el resultado del area segun los datos ingresados al sistema.