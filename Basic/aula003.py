import random

def computerGuess (x, y) :
    trys = y
    low = 1
    high = x
    feedback = ""
    for feedback in range(trys) or feedback == "c":
        computerGuess = random.randint(low, high)
        feedback = input(f"O {computerGuess} é muito alto(a), muito baixo(b) ou esta correto(c)?")
        if feedback == "a" :
            high = computerGuess - 1
        if feedback == "b" :
            low = computerGuess + 1
        if feedback == "c":
            print(f"O computador acertou o numero {computerGuess}!")
            break

        


 
computerGuess(9999, 10)        