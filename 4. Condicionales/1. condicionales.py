'''
Condicionales en Python

Las condicionales permiten tomar desiciones dentro de un programa. Mediante una estructura 
de condiciones segun una condicion sea verdadera o falsa
'''

edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    


#EJEMPLO DE IF - ELSE
edad = 18

if edad >= 18:
    print("Eres Mayor de edad") #Bloque si la condicion es verdadera
else:
    print("Eres menor de edad") #Bloque si la condicion es falsa


# Ejemplo if, elif y else 
nota = 5

if nota == 5:
    print("Excelente")
elif nota >= 4:
    print("Aprobo")
else:
    print("Reprobo")
    