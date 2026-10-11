print("=== Calculadora Segura ===")
print('Digite "sair" para encerrar.\n')

while True:
    entrada = input("Número 1: ").strip()
    if entrada.lower() == "sair":
        print("Encerrando calculadora.")
        break

    try:
        numero1 = float(entrada)
        numero2 = float(input("Número 2: "))
        operacao = input("Operação: ").strip()

        if operacao == "+":
            resultado = numero1 + numero2
        elif operacao == "-":
            resultado = numero1 - numero2
        elif operacao == "*":
            resultado = numero1 * numero2
        elif operacao == "/":
            resultado = numero1 / numero2
        else:
            raise Exception(f"Operação '{operacao}' não suportada. Use +, -, * ou /")
    except ValueError:
        print("Erro: Digite apenas números!")
    except ZeroDivisionError:
        print("Erro: Divisão por zero!")
    except Exception as e:
        print(f"Erro: {e}")
    else:
        print(f"Resultado: {resultado:.2f}")
    finally:
        print("Operação processada.\n")
