#Sistema para um joguinho de advinhe o numero, para o usuario advinhar.

import random

def guess (x, y) :
    random_num = random.randint(1, x)
    guess = 0
    limit = y
    for guess in range(limit) or guess == random_num:
        guess = int(input(f"Advinha um numero de 1 a {x}: "))
        if guess < random_num:
            print("Muito baixo")
        elif guess > random_num:
            print("Muito alto")
    #fim do loop

    if guess != random_num:
        print(f"Voce perdeu! O numero era {random_num}")
    elif guess == random_num:
        print(f"Parabens, voce acertou o numero {random_num}!")

guess(1000, 10)