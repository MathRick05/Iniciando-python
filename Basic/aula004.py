import random

user = input("Escolha (r)pedra, (p)papel, (t)tesoura ou (e)exit:")
computer = random.choice(["r", "p", "t"])

def play(user, computer) :

    while user != "e" :
        print(f"Você escolheu {user}! \
            O computador escolheu {computer}!")
        if user == computer:
            print("Empate!")
        if ((user == "r" and computer == "t") or (user == "p" and computer == "r") or (user == "t" and computer == "p")) :
            print("Voce ganhou!")
        if ((computer == "r" and user == "t") or (computer == "p" and user == "r") or (computer == "t" and user == "p")):
            print("Voce perdeu!")
        if (user == "e"):
            exit()
    
        user = input("Escolha (r)pedra, (p)papel, (t)tesoura ou (e)exit:")
        computer = random.choice(["r", "p", "t"])


play(user, computer)

