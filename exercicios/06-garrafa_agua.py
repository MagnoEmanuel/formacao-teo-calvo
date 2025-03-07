# Venda uma garrafa de água com dois preços diferentes, um para cada tipo de produto.
# Água Mineral Natural = R$1,50
# Água Mineral com Gás = R$1,50

# %%
texto = """ Escolha a sua Água Mineral
(1) Água Mineral Natural
(2) Água Mineral com Gás
"""

opcao = input(texto)

if opcao == "1":
    print("Valor: R$1,50")

elif opcao == "2":
    print("Valor: R$2,50")

else:
    print("Digite uma opção válida!")