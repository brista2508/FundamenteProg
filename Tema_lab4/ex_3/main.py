import random

def joaca_piatra_foarfeca_hartie():
    # Simbolurile jocului
    simboluri = ["piatra", "foarfeca", "hartie"]

    # Scorurile
    scor_utilizator = 0
    scor_calculator = 0

    # Continuarea jocului până când unul dintre jucători câștigă 3 runde
    while scor_utilizator < 3 and scor_calculator < 3:
        alegere_calculator = random.choice(simboluri)
        alegere_utilizator = input("Alegeți un simbol (piatra, foarfeca, hartie): ")

        print(f"Calculatorul a ales: {alegere_calculator}")
        print(f"Ai ales: {alegere_utilizator}")

        # Regulile jocului
        if alegere_utilizator == alegere_calculator:
            print("Egalitate!")
        elif (alegere_utilizator == "piatra" and alegere_calculator == "foarfeca") or \
             (alegere_utilizator == "foarfeca" and alegere_calculator == "hartie") or \
             (alegere_utilizator == "hartie" and alegere_calculator == "piatra"):
            print("Ai câștigat această rundă!")
            scor_utilizator += 1
        else:
            print("Calculatorul a câștigat această rundă!")
            scor_calculator += 1

        print(f"Scorul actual: Utilizator {scor_utilizator} - Calculator {scor_calculator}")

    # Determinarea câștigătorului
    if scor_utilizator == 3:
        print("Ai câștigat jocul!")
    else:
        print("Calculatorul a câștigat jocul!")

joaca_piatra_foarfeca_hartie()
