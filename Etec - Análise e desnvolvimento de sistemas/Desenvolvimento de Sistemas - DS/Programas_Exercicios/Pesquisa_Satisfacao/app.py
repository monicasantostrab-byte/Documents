# Inicio dos contadores

quantidade_excelente = 0
quantidade_ruim = 0

# Pesquisa com os entrevistados

for entrevistado in range(1, 51):

    print(f"\nEntrevistado número {entrevistado}")

    # Solicitação dos dados do entrevistado
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    opiniao = int(input("Opine sobre o atendimento, digite o número correspondente (1-Excelente, 2-Bom, 3-Ruim): "))

    
    if opiniao == 1:
        print("Opinião registrada: EXCELENTE")
        quantidade_excelente += 1

    elif opiniao == 2:
        print("Opinião registrada: BOM")

    elif opiniao == 3:
        print("Opinião registrada: RUIM")
        quantidade_ruim += 1

    else:
        print("Opção inválida!")

# Resultado final

print("\n===== RESULTADO DA PESQUISA =====")
print(f"Total de respostas EXCELENTE: {quantidade_excelente}")
print(f"Total de respostas RUIM: {quantidade_ruim}")