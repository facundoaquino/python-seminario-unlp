from textNumpy import texyNumpy

print(type(texyNumpy))

text_splited = texyNumpy.split('\n')
print(text_splited)

for str in text_splited:
    'https' in str and print(str)
