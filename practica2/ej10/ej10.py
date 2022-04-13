

from functools import reduce
import re


with open('nombres_1.txt', 'r', encoding="UTF-8") as names_1:
    names = names_1.readlines()
with open('eval1.txt', 'r', encoding="UTF-8") as notes1:
    notes = notes1.readlines()
with open('eval2.txt', 'r', encoding="UTF-8") as notes_2:
    notes2 = notes_2.readlines()


def clean_str(names, notes, notes2):
    for inx in range(len(names)):
        names[inx] = re.sub('\'|\n|,', '', names[inx])
        notes[inx] = int(re.sub('\'|\n|,', '', notes[inx]))
        notes2[inx] = int(re.sub('\'|\n|,', '', notes2[inx]))


clean_str(names, notes, notes2)

students_notes = []

for inx in range(len(names)):
    student_note = {'name': names[inx], 'sumNotes': notes[inx]+notes2[inx]}
    students_notes.append(student_note)

average_notes = (reduce(lambda n1, n2: n1+n2, notes) +
                 reduce(lambda n1, n2: n1+n2, notes2)) / len(names)

print(f'El promedio de las notas es de   {round(average_notes,2)}')

for student in students_notes:
    if(student['sumNotes'] < average_notes):
        print(
            f'El alumno  {student["name"]} esta por debajo del promedio con un promedio de {student["sumNotes"]} ')
