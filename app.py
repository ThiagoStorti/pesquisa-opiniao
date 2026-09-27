"""Pesquisa de satisfação do atendimento da TudoWeb."""

excelente = 0
bom = 0
ruim = 0

for i in range(1, 51):
    print(f"\n--- Entrevistado {i} ---")

    nome = input("Nome: ")
    idade = int(input("Idade: "))

    while idade <= 0 or idade > 120:
        idade = int(input("Idade inválida. Digite novamente: "))

    opiniao = int(input("Opinião (1-Excelente | 2-Bom | 3-Ruim): "))

    while not (opiniao == 1 or opiniao == 2 or opiniao == 3):
        opiniao = int(input("Opção inválida. Digite 1, 2 ou 3: "))

    if opiniao == 1 and idade > 0:
        excelente += 1
    elif opiniao == 2:
        bom += 1
    elif opiniao == 3:
        ruim += 1

print("\n===== RESULTADO DA PESQUISA =====")
print(f"EXCELENTE: {excelente}")
print(f"BOM: {bom}")
print(f"RUIM: {ruim}")