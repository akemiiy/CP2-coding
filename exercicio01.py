vogais = "aeiouáéíóúâêôãõà"
consoantes = "bcdfghjklmnpqrstvwxzç"

frase = input("Digite uma frase: ")

total_vogais = 0
total_consoantes = 0

for caractere in frase.lower():
    if caractere in vogais:
        total_vogais += 1
    elif caractere in consoantes:
        total_consoantes += 1

print(f'Frase: "{frase}"')
print(f"Vogais: {total_vogais}")
print(f"Consoantes: {total_consoantes}")
