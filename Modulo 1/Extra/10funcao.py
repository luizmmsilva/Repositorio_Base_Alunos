# Crie uma função que receba o ano do nscimento  e uma pessoa e calcule
# A idade atual(considerar o ano atual fixo, por exemplo 2025)
# Se o voto é 
# negado (menor de 16 anos)
# Opcional/facultativo (16-17 ou acima de 70)
# Obrigátorio (entre 18 a 70 anos)

def verificar_voto(ano_nasc):
    ano_atual = 2025
    idade = ano_atual - ano_nasc
    if idade < 16:
        return idade, "Negado"
    elif idade < 18 or idade >70:
        return idade, "Opcional"
    else:
        return idade, "Obrigatório"
    
ano = int(input("Digite seu ano de nascimento: "))
idade, tipo_voto = verificar_voto(ano)
print(f"Idade: {idade} anos - Voto: {tipo_voto}")
    