import random

# Diferença entre int e round... INT retira a parte decimal "trunca"...   ROUD arredonda
numero_secreto = int(93.90659198/398/2293)
print(numero_secreto)

# Diferença entre int e round... INT retira a parte decimal "trunca"...   ROUD arredonda
numero_secreto = round(93.50659198739872293)
print(numero_secreto)

# random gera um número decimal entre 0 e 1, por isso multiplicamos por 100
numero_secreto = int(random.random() * 100)
print(numero_secreto)

numero_secreto = random.randrange(0,101)
print(numero_secreto)

numero_secreto = random.randint(0,100) # Ele envia isso por randrange e automaticamente já adiciona +1, nao precisando colocar o 101
print(numero_secreto)

numero_secreto = random.randrange(0,11, 2)
print(numero_secreto)