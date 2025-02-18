#Ejercicio 11
año=366
if año>365:
    print("es año bisiesto")
else:
    print("no es año bisiesto ")

#Ejercicio_12
Lista=[2,4,6,8,10]
if len(Lista):
    print(" tiene elementos")
else:
    print(" no tiene elemento")

#Ejercicio_13
multi=15
if multi%3==0 and multi%5==0:
    print(f"{multi} es multiplo de 3 y 5")
else:
    print(f"{multi} no es multiplo de 3 y 5")

#Ejercicio_15
num=12
if num==10:
    print(" la variable tiene valor 10")
else:
    print(" la variable no es de valor 10")

#Ejercicio_14
usuario="cursopython"
contra=123456
usuario_1=input("Ingresa usuario")
contra_1=int(input("Ingresa contraseña"))
if usuario==usuario_1 and contra==contra_1:
    print("Ingresar a cuenta")
else:
    ("Usuario o contraseña incorrectas")


