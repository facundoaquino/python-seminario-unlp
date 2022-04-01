# cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no␣
# ,→contener los símbolos:@ y !):")
# if len(cadena) > 10:
# print("Ingresaste más de 10 carcateres")
# cant = 0
# for car in cadena:
# if car == "@" or car == "!":
# cant = cant + 1
# if cant >= 1:
# print("Ingresaste alguno de estos símbolos: @ o !" )
# else:
# print("Clave válida")


import re


def pass_validate(psw):
    return (not re.search('@|!|\)|\:', psw)) and (len(psw) < 10)


inp_user = input(
    "Ingresa la clave (debe tener menos de 10 caracteres y no␣, →contener los símbolos: @ y !): ")

if(pass_validate(inp_user)):
    print('password ok')
else:
    print('password invalido')
