#Ejercicio_16
nota=59
if nota>=60:
    print("aprobado")
else:
    print("no aprobo")

#Ejercicio_17
pago=2800
if pago>2500:
    print ("es cliente VIP")
elif 1000<=pago<2500:
    print("es cliente plata")
else:
    print("es cliente estandar")

#Ejercicio_18
mensaje=True
if mensaje:
    print("hola gente")
    
#Ejercicio_19
letra="g"
if letra in "aeiou":
    print(f"{letra} es vocal")
else:
    print(f"{letra} es consonante")
    
#Ejercicio_20
a,b,c=2,5,9
if a>b and a>c:
    print(f"{a} es el mayor")
elif b>a and b>c:
    print(f"{b} es el mayor")
else:
    print(f"{c} es el mayor")
