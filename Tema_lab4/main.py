import turtle

character_dict = {
    'A': ['W', 'W', 'S', 'F', 'D', 'G'],
    'B': ['W', 'W', 'S', 'F', 'A', 'D', 'A', 'G'],
    'C': ['D', 'F', 'A', 'G'],
    '.': ['F', 'G'],
    '?': ['W', 'W', 'F', 'S', 'G'],
    '!': ['W', 'A', 'W', 'A', 'F', 'D', 'S', 'G']
}

# Funcție pentru desenarea unui caracter din dicționar
def draw_character(character):
    for instruction in character_dict.get(character, []):
        if instruction == 'W':
            turtle.forward(10)
        elif instruction == 'S':
            turtle.backward(10)
        elif instruction == 'D':
            turtle.right(45)
        elif instruction == 'A':
            turtle.left(45)
        elif instruction == 'F':
            turtle.penup()
            turtle.forward(10)
            turtle.pendown()

def draw_text(text):
    for char in text:
        if char in character_dict:
            draw_character(char)

# Funcție pentru adăugarea unui caracter personalizat la dicționar
def add_character():
    custom_char = input("Introduceți caracterul personalizat: ")
    if custom_char not in character_dict:
        instructions = input("Introduceți instrucțiunile pentru desenare (ex. WSFDG): ")
        character_dict[custom_char] = list(instructions)

def save_characters_to_file():
    with open("characters.txt", "w") as file:
        for char, instructions in character_dict.items():
            file.write(f"{char}:{''.join(instructions)}\n")

# Funcție pentru încărcarea caracterelor personalizate din fișier
def load_characters_from_file():
    try:
        with open("characters.txt", "r") as file:
            for line in file:
                char, instructions = line.strip().split(":")
                character_dict[char] = list(instructions)
    except FileNotFoundError:
        print("Nu s-a găsit fișierul cu caractere personalizate.")

turtle.speed(1)
load_characters_from_file()

while True:
    print("Meniu program:")
    print("1. Desenați mesajul text")
    print("2. Adăugați un caracter nou")
    choice = input("Introduceți opțiunea (1/2): ")

    if choice == '1':
        text = input("Introduceți mesajul text: ")
        turtle.pendown()
        draw_text(text)
        turtle.penup()
    elif choice == '2':
        add_character()
    else:
        print("Opțiune invalidă. Vă rugăm să alegeți din nou.")

    save_characters_to_file()

turtle.done()
