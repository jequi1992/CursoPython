# print("**************************************************")
# print("***********Operaciones con listas***********")
# print("***********Creación de Listas***********")
# print("**************************************************")

# dias=["Lunes","Martes","Miercoles","Jueves","Viernes"]
# print(dias)
# print("**************************************************")

#___________________________________________________________________________________________________________________________________________

# print("**************************************************")
# print("***********Operaciones con listas***********")
# print("***********Creación de Listas***********")
# print("**************************************************")

# lista=[]
# i=1
# Cantidad=int(input("Ingrese la cantidad de numeros a ingresar: "))
# while i<=Cantidad:
#     num=int(input("Ingrese Numero "+str(i)+": "))
#     lista.append(num)
#     i+=1

# print("**************************")
# print("La lista creada es: ",lista)
# print("**************************")

# for i in lista:
#     print(i)

# #___________________________________________________________________________________________________________________________________________

print("*******CREACION LISTAS VACIAS CON FOR*******")
print("**************************************************")

departamentos = []
capitales = []
tamaño=3

for i in range(tamaño):
    print("*******INGRESE DATOS*******")
    departamento=input("Nombre del Departamento ---> "+str(i+1)+":")
    capital=input("Nombre del Capital ---> "+str(i+1)+":")
    departamentos.append(departamento.upper())
    capitales.append(capital.upper())
    print("**************************************************")

#Mostrar la lista

print("************CONSULTANDO DATOS************")
print("*****************************************")

for i in range(tamaño):
    print("CONSULTA -->",i+1)
    print("DEPARTAMENTO: ", departamentos[i]+" ---> CAPITAL: "+capitales[i])
