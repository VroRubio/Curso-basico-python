#Declaramos la variable
calificacion = input ("introduce la calificación de AZ-900: ")
calificacion = int(calificacion)

#Preguntamos si la caclificación es menor a 700
if calificacion <700:
    print("veees por no estudiar") #si es menor a 700 es a esto

elif calificacion > 1000:
    print("Mientes no puedes sacar másde mil")
else: # Si no se cumple ninguno de los if
    print("Felicidades obtuviste tu certificado") #Si es mayor a 700

#Verificador de edad
edad = input("introduce tu edad: ")
edad = int(edad)
if edad >=18 and edad <=100:
    print("Bienbenid@ al MAMITAS")
elif edad > 100:
    print("Si vienes con tus abulitos te podemos fiar")
elif edad < 0 :
    print("Ni quefueras viajer@ de tiempo")
else:
    print("No puedes llevarte esos cigarros")