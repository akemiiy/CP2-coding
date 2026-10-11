especiais = "!@#$%&*"
mensagem = "Digite uma senha: "

while True:
    senha = input(mensagem)

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere in especiais:
            tem_especial = True

    problemas = []
    if len(senha) < 8:
        problemas.append("A senha deve ter no mínimo 8 caracteres")
    if not tem_maiuscula:
        problemas.append("Falta pelo menos 1 letra maiúscula")
    if not tem_minuscula:
        problemas.append("Falta pelo menos 1 letra minúscula")
    if not tem_numero:
        problemas.append("Falta pelo menos 1 número")
    if not tem_especial:
        problemas.append("Falta pelo menos 1 caractere especial (!@#$%&*)")

    if len(problemas) == 0:
        print("Senha válida!")
        break

    print("Senha inválida! Problemas encontrados:")
    for problema in problemas:
        print(f"- {problema}")
    mensagem = "Digite outra senha: "
