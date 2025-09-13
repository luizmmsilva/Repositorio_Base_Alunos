# Crie um programa que verifique se um ano é bissexto. Um ano é bissexto se for divisel por 4
# exceto quando é divisel por 100 e não é por 400

# Etapas 
# 1) Solicitar ao usuario o ano que deseja checar ano

# 2) Fazer a verificação de ano bissexto
# 3) Apresentar a informação ao usuario

ano = int(input(" Digite o ano que deseja checar"))
if (ano % 4 == 0 and ano % 100 !=0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")


