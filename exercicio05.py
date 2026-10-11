texto = input("Digite um texto: ")

contagem = {}
for palavra in texto.lower().split():
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

if len(contagem) == 0:
    print("Nenhuma palavra foi digitada.")
else:
    itens = []
    for palavra, quantidade in contagem.items():
        itens.append((palavra, quantidade))

    for i in range(len(itens)):
        for j in range(len(itens) - 1 - i):
            if itens[j][1] < itens[j + 1][1]:
                itens[j], itens[j + 1] = itens[j + 1], itens[j]

    largura = 0
    for palavra, quantidade in itens:
        if len(palavra) + 2 > largura:
            largura = len(palavra) + 2

    print("=== Contagem de Palavras ===")
    for palavra, quantidade in itens:
        aspas = '"' + palavra + '"'
        if quantidade == 1:
            print(f"{aspas:<{largura}} → {quantidade} vez")
        else:
            print(f"{aspas:<{largura}} → {quantidade} vezes")

    mais_frequente, maior_quantidade = itens[0]
    print(f'\nPalavra mais frequente: "{mais_frequente}" ({maior_quantidade} vezes)')
    print(f"Total de palavras únicas: {len(contagem)}")
