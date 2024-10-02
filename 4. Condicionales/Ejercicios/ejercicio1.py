'''
Hacer un programa donde se ingrese un numero de 0 a 100, si la nota es mayor-igual a 60
aprobo la materia.
'''

calificacion = float(input("Ingresar una nota entre 0 y 100 "))

if calificacion > 100 or calificacion < 0:
    print("La nota es incorrecta")
elif calificacion >= 60 and calificacion <= 100:
    print(f"El estudiante aprobo, NOTA {calificacion}")
else:
    print(f"El estudando reprobo, NOTA {calificacion}")
    