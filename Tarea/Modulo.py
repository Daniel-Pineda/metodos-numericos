def suma(numUno, numDos):

	resultado = numUno + numDos

	return resultado

def resta(numUno, numDos):

	resultado = numUno - numDos

	return resultado	

def division(numUno, numDos):
	
	if numDos <= 0:
		while numDos <= 0:
			numDos = int(input("Ingresa un valor mayor a cero: "))

	return numUno / numDos			


def multiplicacion(numUno, numDos):

	resultado = numUno * numDos

	return resultado	