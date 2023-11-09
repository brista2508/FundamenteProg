def remove_duplicates(input_numbers):
    unique_numbers = []
    for number in input_numbers.split():
        if number not in unique_numbers:
            unique_numbers.append(number)
    return ' '.join(unique_numbers)

input_numbers = input("Introdu o lista de numere de forma 'xy' separate prin spatii: ")
result = remove_duplicates(input_numbers)
print("Rezultatul dupa ce au fost eliminate duplicatele: ", result)

# 12 23 54 12 38 76 34 21