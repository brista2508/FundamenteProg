def find_longest_domino_sequence(numbers):
    longest_sequence = []
    current_sequence = [numbers[0]]

    for i in range(1, len(numbers)):
        x1, y1 = map(int, current_sequence[-1])
        x2, y2 = map(int, numbers[i])

        if y1 == x2:
            current_sequence.append(numbers[i])
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            current_sequence = [numbers[i]]

    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence

    return longest_sequence

input_numbers = input("Introdu o lista de numere de forma 'xy' separate prin spatii: ").split()
domino_sequence = find_longest_domino_sequence(input_numbers)

if domino_sequence:
    print("Cea mai lunga secventa de domino:", ' '.join(domino_sequence))
else:
    print("Nici o secventa de domino gasita.")


# 12 23 54 12 38 76 34 21