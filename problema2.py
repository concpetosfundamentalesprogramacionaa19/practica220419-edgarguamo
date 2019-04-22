"""

	Enunciado:
	Se desea realizar un prigrama que permita calcular el
	valor mensual a pagar a un trabajador; así como también 
	el valor de su descuento al seguro Social (10% del total a pagar). 
	El sueldo mensual del trabajador se obtiene mediante una
	multiplicación simple entre el número de horas (100), por
	el costo hora oficial
	Ejercicio2 python
	Autor: Edgar Guamo
"""
print("Bienvenido al comprobante de sueldo de Andes S.")
		 
#Petición de variables por teclado
tiempo = input("Por favor Ingrese el número de horas trabajadas: ")
hora = input("Por  favor ingrese el valor por hora: ")

#Transformación de string a float
tiempo = float (tiempo)
hora = float (hora)

#Operaciones
sueldo = tiempo * hora
seguro = sueldo * 0.10  # 10% (0,10) del sueldo es para el seguro  
sueldo = sueldo - seguro

#Impresion del resultado
print ("Estimado usuario su salario mensual es de: $ %.2f \n\
	Su aporte al Seguro Social es de: $%.2f" %(sueldo, seguro)) 

