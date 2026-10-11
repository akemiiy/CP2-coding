logs = [
    "[2025-02-20 08:15:01] [INFO] Login ok - IP: 192.168.1.10",
    "[2025-02-20 08:15:03] [WARNING] Area restrita - IP: 10.0.0.5",
    "[2025-02-20 08:15:10] [ERROR] Falha auth - IP: 185.220.101.1",
    "[2025-02-20 08:15:15] [INFO] Arquivo acessado - IP: 192.168.1.10",
    "[2025-02-20 08:15:22] [ERROR] Conexao recusada - IP: 185.220.101.1",
    "[2025-02-20 08:15:30] [WARNING] Certificado SSL - IP: 172.16.0.3",
    "[2025-02-20 08:15:35] [ERROR] Falha auth - IP: 10.0.0.5",
    "log malformado sem formato correto",
    "[2025-02-20 08:15:45] [ERROR] Timeout - IP: 185.220.101.1",
    "[2025-02-20 08:15:50] [WARNING] CPU alta - IP: 192.168.1.20",
    "[2025-02-20 08:16:01] [ERROR] Falha auth - IP: 185.220.101.1",
    "[2025-02-20 08:16:05] [INFO] Firewall ok - IP: 192.168.1.10",
]

contagem = {"INFO": 0, "WARNING": 0, "ERROR": 0}
erros_por_ip = {}
eventos = []
malformados = 0

for log in logs:
    try:
        nivel = log.split("] [")[1].split("]")[0]
        mensagem = log.split("] ")[2].split(" - IP:")[0]
        ip = log.split("IP: ")[1].strip()
        if nivel not in contagem:
            raise ValueError(f"Nível desconhecido: {nivel}")
    except IndexError:
        malformados += 1
    except ValueError:
        malformados += 1
    else:
        eventos.append({"nivel": nivel, "ip": ip, "mensagem": mensagem})
        contagem[nivel] += 1
        if nivel == "ERROR":
            if ip in erros_por_ip:
                erros_por_ip[ip] += 1
            else:
                erros_por_ip[ip] = 1

print("=== Relatório de Logs ===")
for nivel, total in contagem.items():
    print(f"{nivel + ':':<9}{total} eventos")
print(f"Logs malformados: {malformados}")

if len(erros_por_ip) == 0:
    print("\nNenhum erro registrado.")
else:
    ranking = []
    for ip, total in erros_por_ip.items():
        ranking.append((ip, total))

    for i in range(len(ranking)):
        for j in range(len(ranking) - 1 - i):
            if ranking[j][1] < ranking[j + 1][1]:
                ranking[j], ranking[j + 1] = ranking[j + 1], ranking[j]

    ip_top, total_top = ranking[0]
    print(f"\nIP com mais erros: {ip_top} ({total_top} erros)")

    largura = 0
    for ip, total in ranking:
        if len(ip) > largura:
            largura = len(ip)

    print("\nDetalhamento de erros:")
    for ip, total in ranking:
        if total == 1:
            print(f"  {ip:<{largura}} → {total} erro")
        else:
            print(f"  {ip:<{largura}} → {total} erros")
