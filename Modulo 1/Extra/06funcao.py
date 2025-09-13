# Crie uma funçao que iddentifique 
# se um número é par ou ìmpar

n = int(input("Digite um número: "))

def par_impar(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
print(par_impar(n))
