from colorama import Fore, Style, init

init()

niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]
def definir_cor(nivel):

    if nivel == 1:
        return Fore.RED

    elif nivel == 2:
        return Fore.YELLOW

    elif nivel == 3:
        return Fore.GREEN

    elif nivel == 4:
        return Fore.CYAN

    elif nivel == 5:
        return Fore.BLUE
    
# Exibi as situações do reservatório

print("===== MONITORAMENTO DO RESERVATÓRIO =====\n")

for numero, situacao in enumerate(niveis, start=1):

    # Chama a função para identificar a cor

    cor = definir_cor(numero)

    # Exibe a mensagem com a cor correspondente

    print(f"{cor}Nível {numero}: {situacao}{Style.RESET_ALL}")

