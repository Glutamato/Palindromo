

#TERCER PASO DONDE SE PONE LA PRIMERA FUNCIÓN DEFINIDA
#SE DETALLA LA FUNCIÓN DE 2 palindromo()
#primero elimino posibles espacios
#segundo cambio posibles mayúsculas a minusculas
#genero una palabra invertida (sin espacios y en minusculas)
#comparo palabra vs palabra_invertida

def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


#SEGUNDO PASO DE PROGRAMACIÓN Y DE LOGICA DEL CODIGO
#recibo la palabra y evaluo si es palíndromo

def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palÃ­ndromo')
    else:
        print('No es palÃ­ndromo')


#PRIMER PASO DE CODIFICACIÓN
#se da iniciación

if __name__ == '__main__':
    run()
