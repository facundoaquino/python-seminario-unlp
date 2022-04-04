import collections
from typing import Counter

frase = """
Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple.
"""

text_lower = frase.lower()
# IMPLEMENTACION ITERATIVA CON COUNTER FILTER Y MAP

counter_words = Counter(text_lower.split()).items()
print(counter_words)
filtered_words = list(filter(lambda w: w[1] == 1, (counter_words)))
list_words = list(map(lambda w: w[0], filtered_words))
for word in list_words:
    print(word)


# IMPLEMENTACION CON SET

set_unique_words = list(set(text_lower.split()))
print(set_unique_words)
