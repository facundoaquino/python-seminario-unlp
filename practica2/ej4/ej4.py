from random import randrange


evaluar = """título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures"""


def separate_text(text):
    return evaluar.split('título:')[1].split('resumen:')


def rank_orations(resume, text_counter):
    orations = resume.split('.')
    for oration in orations:
        len_oration = len(oration.split())
        match len_oration:
            case  0 | 1 | 2:
                text_counter['easy_read'] += 1
        if len_oration <= 12:
            text_counter['easy_read'] += 1
        elif len_oration <= 17:
            text_counter['aceptable_read'] += 1
        elif len_oration <= 25:
            text_counter['hard_read'] += 1
        else:
            text_counter['very_hard_read'] += 1


def analize_text(title, resume):
    text_counter = {'title_ok': False, 'easy_read': 0,
                    'aceptable_read': 0, 'hard_read': 0, 'very_hard_read': 0}
    text_counter['title_ok'] = len(title.split()) <= 10
    rank_orations(resume, text_counter)
    return text_counter


def show_messages(result):
    if(result['title_ok']):
        print('el titulo esta ok')
    else:
        print('el titulo no esta ok')
    print(
        f'cantidad de oraciones faciles de leer : {result["easy_read"]} , aceptables de leer {result["aceptable_read"]} ,dificil de leer: {result["hard_read"]}, muy dificil de leer {result["very_hard_read"]}')
    return


[title, resume] = separate_text(evaluar)

result = analize_text(title, resume)
print(result)
show_messages(result)
