'''
7. Escriba un programa que solicite que se ingrese una palabra o frase y permita identificar si la
misma es un Heterograma (tenga en cuenta que el contenido del enlace es una traducción del
inglés por lo cual las palabras que nombra no son heterogramas en español). Un Heterograma
es una palabra o frase que no tiene ninguna letra repetida entre sus caracteres.
Tener en cuenta - Lo que no se puede repetir en la frase son sólo aquellos caracteres que sean
letras. - No se distingue entre mayúsculas y minúsculas, es decir si en la frase o palabra tenemos
la letra “T” y la letra “t” la misma NO será un Hererograma. - Para simplificar el ejercicio vamos
a tomar como que las letras con tilde y sin tilde son distintas. Ya que Python las diferencia:
'''


import re
import string
from collections import Counter

all_letters = string.ascii_letters

phrase = input(
    ' Ingrese una palabra o frase para saber si es un heterograma\n').lower()

print(re.sub('[^a-z]', '', phrase))

# implementacion con set

unique_letters = set(phrase)
if(len(unique_letters) == len(phrase)):
    print('la palabra o frase   es un heterograma')
else:
    print('la palabra o frase  NO es un heterograma')

# IMPLEMENTACION CON COUNTER

counter_char = Counter(phrase)
all_uniques = not ((counter_char.most_common()[0][1]) > 1)
if(all_uniques):
    print('la palabra o frase   es un heterograma')
else:
    print('la palabra o frase  NO es un heterograma')


#  implementacion iterativa con espacio auxiliar
coincidences = []
for letter in phrase:
    if(letter in coincidences):
        print('la palabra o frase No es un heterograma')
        break
    else:
        coincidences.append(letter)

if(len(phrase) == len(coincidences)):
    print('la palabra o frase   es un heterograma')
