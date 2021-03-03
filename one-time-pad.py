"""
Universidad del Valle de Guatemala
Seguridad en sistemas de computación
Catedrático: Melinton Navas
Pablo Viana - 16091
Dieter de Wit - 15146

Programa para simular una comunicación encriptada por el método one-time-pad, que acepta cadenas de catacteres
menores a 27, sin espacios.

Código basado en implementación anterior de albohlabs https://github.com/albohlabs/one-time-pad
"""

import string
import random
import sys

# obtenemos los caracteres del abecedario en minuscula
abecedario = string.ascii_lowercase
one_time_pad = list(abecedario)

help = """ejecute los siguiente comandos para:

Encriptar: python one-time-pad.py -e
Desencriptar: python one-time-pad.py -d
"""


def encriptar(mensaje, llave):
    texto_encriptado = ''
    for index, char in enumerate(mensaje):
        # buscamos el indice del primer caracter del mensaje en el abecedario
        char_index = abecedario.index(char)
        # Buscamos el indice del caracter encontrado en el arreglo llave[posicion indice en que va el ciclo]
        llave_index = one_time_pad.index(llave[index])

        # realizamos el cifrado
        encriptado = (char_index + llave_index) % len(one_time_pad)
        # armamos la palabra encriptada
        texto_encriptado += abecedario[encriptado]

    return texto_encriptado


def desencriptar(mensaje, llave):
    # Revisa que los parametros sean strings validos para no computar un string vacio
    if mensaje == '' or llave == '':
        return ''

    # Tomamos el indice del primer caracter del mensaje en el abecedario
    char_index = abecedario.index(mensaje[0])
    # Tomamos el indice del primer caracter de la llave en el abecedario
    llave_index = one_time_pad.index(llave[0])

    # Realizamos el Desencriptado
    desencriptado = (char_index - llave_index) % len(one_time_pad)
    # Buscamos un solo caracter desencriptado en el abecedario
    character = abecedario[desencriptado]

    # Recursivamente, buscamos los demas caracteres en el abecedario
    return character + desencriptar(mensaje[1:], llave[1:])


if __name__ == '__main__':
    availableOpt = ["-d", "-e"]
    if len(sys.argv) == 1 or sys.argv[1] not in availableOpt:
        print(help)
        exit(0)

    mensaje = input("mensaje: ")

    if sys.argv[1] == availableOpt[1]:
        dict_llave = list(string.ascii_lowercase)
        random.shuffle(dict_llave)
        llave = dict_llave[:len(mensaje)]
        llave_txt = ''.join([str(elem) for elem in llave])
        text_file = open("llave.txt", "w")
        text_file.write(llave_txt)
        text_file.close()
        print(encriptar(mensaje, llave))
    elif sys.argv[1] == availableOpt[0]:
        text_file = open("llave.txt", "r")
        llave = text_file.read()
        print(desencriptar(mensaje, llave))
