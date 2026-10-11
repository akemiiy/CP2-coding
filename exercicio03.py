ips = ["192.168.1.1", "10.0.0.5", "172.16.0.3"]

while True:
    print("\n=== Gerenciador de IPs ===")
    print("[1] Adicionar IP")
    print("[2] Remover IP")
    print("[3] Listar todos")
    print("[4] Buscar IP")
    print("[5] Sair")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        ip = input("IP para adicionar: ").strip()
        if ip == "":
            print("IP inválido!")
        elif ip in ips:
            print("IP já existe na lista!")
        else:
            ips.append(ip)
            print("IP adicionado!")

    elif opcao == "2":
        ip = input("IP para remover: ").strip()
        if ip in ips:
            ips.remove(ip)
            print("IP removido!")
        else:
            print("IP não encontrado")

    elif opcao == "3":
        if len(ips) == 0:
            print("A lista está vazia.")
        else:
            for i in range(len(ips)):
                print(f"{i + 1}. {ips[i]}")

    elif opcao == "4":
        ip = input("IP para buscar: ").strip()
        posicao = 0
        for i in range(len(ips)):
            if ips[i] == ip:
                posicao = i + 1
                break
        if posicao > 0:
            print(f"IP encontrado na posição {posicao}")
        else:
            print("IP não encontrado")

    elif opcao == "5":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
