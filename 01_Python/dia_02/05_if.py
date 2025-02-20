#IF ELSE ELIF
#%%
idade = 17

if idade >= 18:
    print("Você pode beber whisky!")

if idade <= 17:
    print("Você não pode beber álcool")

#ELSE
#%%
idade = 17

if idade >= 70:
    print("Você pode beber whisky!")
    print("Cuidado com os rins.")

elif idade >= 18:
    print("Você pode beber whisky!")

elif idade <= 17:
    print("Você não pode beber álcool!")
    print("Que tal um refri?")

else:
    print("Você não pode beber álcool.")