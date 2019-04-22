"""

	Ejercicio de python 1
	Usuario: Edgar Guamo

"""

print ("Bienvenido al procesador de ejercicio estático")
x = input("Por favor ingrese la variable x")
y = input("Por favor ingrese la variable y")
z = input("Por favor ingrese la variable z")
#Obtención de variables mediante teclado y tranformación a int 

#Transformación de variables 
x = float (x)
y = float (y)
z = float (z)

#Fórmula 
m = (x + (y/z))/ (x-(y/z))

#Impresion
print("El valor de m, en base a las variables es : x= \n%.1f\n\t\
	y= %.1f \n\t\t\tz= %.1f\nDa como resultado \n\t\t\t\tm= %.1f" 
	% (x, y, z, m))

