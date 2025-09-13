# Crie um programa que calcule o fatorial de um número 

n= int(input("Digite um número para saber o fatorial: "))
resultado = 1 # 5! = 5.4.3.2.1 => a variavel é o n:
f = 1

while f<=n:
    resultado *= f 
    f += 1 # f = f+1
    print(f"O fatorial do numero {n} é {resultado}.")
    