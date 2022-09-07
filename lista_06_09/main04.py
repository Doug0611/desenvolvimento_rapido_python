numbers = []

for i, number in enumerate(range(20), start=1):
    numbers.append(int(input(f'{i}º número: ')))
    
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers  = list(filter(lambda x: not x % 2 == 0, numbers))

print(f'Números pares: {even_numbers}.')
print(f'Números ímpares: {odd_numbers}.')
print(f'Números: {numbers}.')
