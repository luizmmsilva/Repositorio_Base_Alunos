# Crie um programa referente a quantidade de bombons

bombons = 100

while bombons > 0 : # enqaunto bombons > 0 o while continua executando
    print(f"Eu tenho {bombons} bombons. ") # informar o número de bombons atual
    bombons -= 1 # DIminui a quantidade de bombons por loop
    print(f"Comi 1 e fiquei com {bombons} bombons.") # informa a quantidade de bombons após a subtração
    if bombons == 0: # Quando a quantidade de bombons for zero
        print("Acabaram os bombons")