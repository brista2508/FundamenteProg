import turtle

cestoasa = turtle.Turtle()

dict = {}

def draw_(text):
    for litera in text:
        for operatie in dict[litera]:
            if operatie == 'W':
                cestoasa.forward(10)
            elif operatie == 'S':
                cestoasa.backward(10)
            elif operatie == 'L':
                cestoasa.left(45)
            elif operatie == 'R':
                cestoasa.right(45)
            elif operatie == 'F':
                cestoasa.penup()
            elif operatie == 'G':
                cestoasa.pendown()

def load_chars():
    try:
        with open("dict.out",'r') as file:
            for line in file:
                char,instructions = line.strip().split(':')
                dict[char] = list(instructions)
    except FileNotFoundError:
        print("Nu s-a găsit fișierul cu caractere personalizate.")


def add_char():
    codificare = input("Caracter nou ")
    if codificare not in dict:
        instructions = input("Introduceți instrucțiunile pentru desenare (ex. WSFDG): ")
        dict[codificare] = list(instructions)
    else:
        exit(0)

def save_characters_to_file():
    with open("dict.out", "w") as file:
        for char, instructions in dict.items():
            file.write(f"{char}:{''.join(instructions)}\n")

def init():
    cestoasa.penup()
    cestoasa.backward(750)
    cestoasa.pendown()
    dict[' '] = ['F','W','W','W','W','W','G']

load_chars()

init()

cestoasa.speed(5)

print("1. Desenați mesajul text")
print("2. Adăugați un caracter nou")
choice = int(input("Introduceți opțiunea (1/2): "))

if choice == 1:
    text = input("Introdu textul : ")
    draw_(text)
else:
    add_char()

save_characters_to_file()

turtle.done()