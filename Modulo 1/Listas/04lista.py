# Criar uma lista com as informações

alunos = [
    {"nome":"João", "idade":20, "nota":7.5},
    {"nome":"Maria", "idade":18, "nota":8.2},
    {"nome":"Pedro", "idade":19, "nota":7.5},
    {"nome":"Vivi", "idade":21, "nota":9.0},
    {"nome":"Luizinho", "idade":18, "nota":10}
]

# Criar 2 variaveis
total_notas = 0 # essa varaiavel será nosso contador para somar as notas
quantidade_alunos = len(alunos) # essa variavel vai informar a quantidade dos alunos

for aluno in alunos: # esse for ira percorrer cada objeto da lista
    total_notas += aluno["nota"] # aqui eu somo cada nota
media_notas = total_notas/quantidade_alunos # fazemos o cálculo da média
print(f"A média das notas dos alunos é {media_notas:.2f}")
