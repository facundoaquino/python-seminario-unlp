import string


text = 'Python define en PEP8  como como como guía de estilos base y en PEP257 la convención para Docstrings. Teniendo esta referencia vamos a mencionar las normas mas importantes que esperamos que traten de cumplir en el trabajo.'


def is_a_letter(c):
    return c in string.ascii_letters


letter = input('queres ver todas las palabras que empiexen con la letra...')

if is_a_letter(letter):
    text_splited = text.lower().split(' ')
    filtered_words = set(
        list(filter(lambda w: w.startswith(letter), text_splited)))
    for word in filtered_words:
        print(f'la palabra  {word} empieza con {letter}')
    len(filtered_words) or print(
        f'ninguna palabra empieza con la letra {letter}')
else:
    print('no ingresaste una letra valida')
