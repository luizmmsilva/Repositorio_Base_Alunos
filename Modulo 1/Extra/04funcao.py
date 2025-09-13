# Crie uma função que some 
# valoresa ao numero pi

#neses trecho de código
# o argumento b está definido

def soma_valores(a, b=3.14):
    return a + b
print(soma_valores(10)) # passamos apenas um argumento 
# por que o outro já foi pré definido

def soma_valores(a , b):
    return a + b
print(soma_valores(2,10))