questions = [
    'Telefonou para a vítima ?',
    'Esteve no local do crime ?',
    'Mora perto da vítima ?',
    'Devia para a vítima ?',
    'Já trabalhou para a vítima ?'
]

answers = []

for question in questions:
    print(question)
    answer = int(input(
            '\033[1;92m1 - PARA SIM\033[m' +
            ' / ' + '\033[1;91m0 - PARA NÃO\033[m: '
        ))
    if answer < 0 or answer > 1:
        raise ValueError(
            'only 1 for positive response or 0 for negative response'
        )
    answers.append(answer)

if answers.count(1) < 2:
    print("\033[1;92m\nInocente\033[m")
elif answers.count(1) == 2:
    print("\033[1;33m\nSuspeito\033[m")
elif answers.count(1) == 3 or answers.count(1) == 4:
    print("\033[1;35m\nCúmplice\033[m")
elif answers.count(1) == 5:
    print("\033[1;31m\nAssassino\033[m")