print("============================")
print("MENU OPERACIONES MATEMATICAS")
print("============================")
print("1 Suma")
print("2 Resta")
print("3 Multiplicación")
print("4 División")
print("5 Salir")

opc=int(input("Ingrese el numero de la operación matematica que desee realizar: "))

if opc==1:
   numero_1=float(input("Ingrese el número 1: ")) # Esta variable guarda el valor del numero 1
   numero_2=float(input("Ingrese el número 2: ")) # Esta variable guarda el valor del numero 2
   suma=numero_1+numero_2
   print("El resultado de la suma es ",suma)
elif opc==2:
   numero_1=float(input("Ingrese el número 1: ")) # Esta variable guarda el valor del numero 1
   numero_2=float(input("Ingrese el número 2: ")) # Esta variable guarda el valor del numero 2
   resta=numero_1-numero_2
   print("El resultado de la resta es ",resta)
elif opc==3:
   numero_1=float(input("Ingrese el número 1: ")) # Esta variable guarda el valor del numero 1
   numero_2=float(input("Ingrese el número 2: ")) # Esta variable guarda el valor del numero 2
   multiplicacion=numero_1*numero_2
   print("El resultado de la Multiplicación es ",multiplicacion)
elif opc==4:
   numero_1=float(input("Ingrese el número 1: ")) # Esta variable guarda el valor del numero 1
   numero_2=float(input("Ingrese el número 2: ")) # Esta variable guarda el valor del numero 2
   division=round(numero_1/numero_2,2)
   print("El resultado de la división es ",division)
elif opc==5:
    exit
else:
    print("El valor ingresado es incorrecto, Verifique y vuelva a intentarlo")