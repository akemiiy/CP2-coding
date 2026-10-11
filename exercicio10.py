import random

senhas = {
    "gmail": "MinhaS3nha!",
    "github": "Dev@2024Seguro",
    "banco_dados": "db123",
}

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
especiais = "!@#$%&*"

while True:
    print("\n=== Gerenciador de Senhas ===")
    print("[1] Cadastrar senha")
    print("[2] Listar serviços")
    print("[3] Buscar senha por serviço")
    print("[4] Gerar senha aleatória")
    print("[5] Avaliar força de todas as senhas")
    print("[6] Exportar relatório")
    print("[7] Sair")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        servico = input("Serviço: ").strip().lower()
        senha = input("Senha: ")
        try:
            if servico == "" or senha == "":
                raise ValueError("Serviço e senha não podem ser vazios!")
            if servico in senhas:
                raise ValueError("Serviço já cadastrado!")
        except ValueError as e:
            print(f"Erro: {e}")
        else:
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

            if len(senha) < 8:
                forca = "Fraca"
            elif tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
                forca = "Forte"
            elif (tem_maiuscula or tem_minuscula) and tem_numero:
                forca = "Média"
            else:
                forca = "Fraca"

            senhas[servico] = senha
            print(f"Cadastrado! Força: {forca}")

    elif opcao == "2":
        if len(senhas) == 0:
            print("Nenhum serviço cadastrado.")
        else:
            numero = 1
            for servico in senhas:
                print(f"{numero}. {servico}")
                numero += 1

    elif opcao == "3":
        servico = input("Serviço: ").strip().lower()
        try:
            senha = senhas[servico]
        except KeyError:
            print("Erro: Serviço não encontrado!")
        else:
            print(f"Senha de {servico}: {senha}")

    elif opcao == "4":
        try:
            tamanho = int(input("Tamanho da senha: "))
            if tamanho <= 0:
                raise ValueError
        except ValueError:
            print("Erro: Digite um número inteiro maior que zero!")
        else:
            senha_gerada = ""
            for i in range(tamanho):
                senha_gerada += random.choice(caracteres)
            print(f"Senha gerada: {senha_gerada}")

    elif opcao == "5":
        if len(senhas) == 0:
            print("Nenhuma senha cadastrada.")
        else:
            for servico, senha in senhas.items():
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

                if len(senha) < 8:
                    forca = "Fraca"
                elif tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
                    forca = "Forte"
                elif (tem_maiuscula or tem_minuscula) and tem_numero:
                    forca = "Média"
                else:
                    forca = "Fraca"

                aspas = '"' + senha + '"'
                print(f"{servico + ':':<13}{aspas:<18}→ {forca}")

    elif opcao == "6":
        try:
            with open("senhas_relatorio.txt", "w") as arquivo:
                arquivo.write("=== Relatório de Senhas ===\n")
                for servico, senha in senhas.items():
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

                    if len(senha) < 8:
                        forca = "Fraca"
                    elif tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
                        forca = "Forte"
                    elif (tem_maiuscula or tem_minuscula) and tem_numero:
                        forca = "Média"
                    else:
                        forca = "Fraca"

                    arquivo.write(f"{servico}: {forca}\n")
                arquivo.write(f"Total de serviços: {len(senhas)}\n")
        except OSError as e:
            print(f"Erro ao exportar: {e}")
        else:
            print("Relatório exportado com sucesso!")

    elif opcao == "7":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
