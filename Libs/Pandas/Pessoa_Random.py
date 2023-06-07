import random

lista_nomes_m=[
    'Arthur',
    'Bruno',
    'Carlos',
    'Daniel',
    'Eitor',
    'Felipe',
    'Gustavo',
    'Hilster',
    'Henrique',
    'Iago',
    'Jader',
    'Kenedi',
    'Lucas',
    'Manuel',
    'Nelson',
    'Osmar',
]
lista_nomes_f=[
    'Amanda',
    'Bruna',
    'Carla',
    'Debora',
    'Elena',
    'Fátima',
    'Gabrieli',
    'Helen',
    'Jackeline',
    'Ketlin',
    'Letícia',
    'Maria',
    'Natália',
    'Patrícia',
    'Talia',
]

lista_segundo_nome=[
    None,    
    
]
lista_sobrenomes=[
    'Almeida',
    'Barbosa',
    'Carvalho',
    'Dal',
    'Santos',
    'Cunha',
    
]

def pessoa_componentes():
    return {'Nome':'primeiro_nome','Sobrenome':'sobrenome',
            'Sexo':'sexo','Altura':'altura','Idade':'idade'}
def pessoa():
    i=random.randint(0,1)
    primeiro_nome=random.choice(lista_nomes_f if i == 1 else lista_nomes_m)
    if random.randint(0,4) == 0:
        primeiro_nome+=f' {random.choice(lista_nomes_f if i == 1 else lista_nomes_m)}'
    t=random.randint(0,4) == 0
    sobrenome=[random.choice(lista_sobrenomes) for i in range(random.randint(1,5) if t  else 2)]
    sobrenome=' '.join(sobrenome)
    sexo='F' if i == 1 else 'M'
    return {'Nome':primeiro_nome,'Sobrenome':sobrenome,'Sexo':sexo,'Altura':random.randint(100,200)/100,'Idade':random.randint(13,80)}
    
