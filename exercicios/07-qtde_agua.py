# %%
texto = """ Escolha a sua Água Mineral
(1) Água Mineral Natural
(2) Água Mineral com Gás
"""

opcao = input(texto)

valor_item = 0

if opcao == "1":
    valor_item = 1.5
elif opcao == "2":
    valor_item = 2.5

if valor_item == 0:
    print("Digite uma opção válida!")

else:
    qtde = input("Quantidade de Garrafas: ")
    qtde = int(qtde)
    valor_total = qtde * valor_item
    print("Valor Total: ", valor_total)