ativos = [
    {"nome": "SRV-WEB01", "tipo": "servidor", "ip": "192.168.1.10", "status": "ativo"},
    {"nome": "PC-RH03", "tipo": "estacao", "ip": "192.168.1.45", "status": "ativo"},
    {"nome": "SW-CORE01", "tipo": "switch", "ip": "192.168.1.1", "status": "inativo"},
]

tipos_validos = ["servidor", "estacao", "switch", "roteador"]
status_validos = ["ativo", "inativo"]

while True:
    print("\n=== Inventário de Ativos ===")
    print("[1] Cadastrar ativo")
    print("[2] Listar ativos")
    print("[3] Buscar por IP")
    print("[4] Alterar status")
    print("[5] Remover ativo")
    print("[6] Sair")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        try:
            nome = input("Nome: ").strip()
            if nome == "":
                raise ValueError("Erro: Nome não pode ser vazio!")
            tipo = input("Tipo (servidor/estacao/switch/roteador): ").strip().lower()
            if tipo not in tipos_validos:
                raise ValueError("Erro: Tipo inválido!")
            ip = input("IP: ").strip()
            if ip == "":
                raise ValueError("Erro: IP não pode ser vazio!")
            for ativo in ativos:
                if ativo["ip"] == ip:
                    raise ValueError("Erro: IP já cadastrado!")
            status = input("Status (ativo/inativo): ").strip().lower()
            if status not in status_validos:
                raise ValueError("Erro: Status inválido!")
        except ValueError as e:
            print(e)
        else:
            ativos.append({"nome": nome, "tipo": tipo, "ip": ip, "status": status})
            print("Cadastrado!")

    elif opcao == "2":
        if len(ativos) == 0:
            print("Nenhum ativo cadastrado.")
        else:
            print(f"{'NOME':<12} {'TIPO':<10} {'IP':<15} STATUS")
            for ativo in ativos:
                print(f"{ativo['nome']:<12} {ativo['tipo']:<10} {ativo['ip']:<15} {ativo['status']}")
            print(f"Total: {len(ativos)} ativos")

    elif opcao == "3":
        ip = input("IP: ").strip()
        try:
            encontrado = None
            for ativo in ativos:
                if ativo["ip"] == ip:
                    encontrado = ativo
                    break
            if encontrado is None:
                raise ValueError("Ativo não encontrado")
        except ValueError as e:
            print(e)
        else:
            print(f"Nome:   {encontrado['nome']}")
            print(f"Tipo:   {encontrado['tipo']}")
            print(f"IP:     {encontrado['ip']}")
            print(f"Status: {encontrado['status']}")

    elif opcao == "4":
        ip = input("IP: ").strip()
        try:
            encontrado = None
            for ativo in ativos:
                if ativo["ip"] == ip:
                    encontrado = ativo
                    break
            if encontrado is None:
                raise ValueError("Ativo não encontrado")
            novo_status = input("Novo status (ativo/inativo): ").strip().lower()
            if novo_status not in status_validos:
                raise ValueError("Erro: Status inválido!")
        except ValueError as e:
            print(e)
        else:
            encontrado["status"] = novo_status
            print("Status atualizado!")

    elif opcao == "5":
        ip = input("IP: ").strip()
        try:
            encontrado = None
            for ativo in ativos:
                if ativo["ip"] == ip:
                    encontrado = ativo
                    break
            if encontrado is None:
                raise ValueError("Ativo não encontrado")
        except ValueError as e:
            print(e)
        else:
            ativos.remove(encontrado)
            print("Ativo removido!")

    elif opcao == "6":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
