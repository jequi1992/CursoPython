#-------------------------------------------------------------------------------------------------------#

i=1
while i<=3:
  print(i)
  i+=1
print("Programa terminado")

#-------------------------------------------------------------------------------------------------------#
print("========================")
print("*****USO DEL WHILE******")
print("========================")

num=0
while num<=10:
  print(f"El numero es --> {num}")
  num+=1

#-------------------------------------------------------------------------------------------------------#
print("=============================================")
print("*****USO DEL WHILE - VALIDAR CONTRASEÑA******")
print("=============================================")

clave ="Python"
oportunidad = 1
while oportunidad <=3:
  contra=input("Ingrese Contraseña ---> ")
  if contra==clave:
     print("Clave Correcta")
     print("==============")
     valida=True
     break
  elif contra != clave:
    print("Clave Incorrecta")
    print("==============")
    valida= False
    oportunidad=oportunidad+1
  
if valida==True:
  print("========================")
  print("Puede ingresar al sistema")
  print("========================")
else:
  print("========================")
  print("Ya supero los intentos permitidos")
  print("========================")
