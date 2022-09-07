ages = []
heights = []

for i, n in enumerate(range(5), start=1):
    ages.append(int(input(f'Informe a idade da {i}º pessoa: ')))
    heights.append(float(input(f'Informe a altura {i}º pessoa : ')))
    print('*****' * 4)

ages_reverse = sorted(ages,  reverse=True)
heights_reverse = sorted(heights, reverse=True)

print(f'\nIdades: {ages_reverse} - Alturas: {heights_reverse}.')
