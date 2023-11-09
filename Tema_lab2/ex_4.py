def encrypt_list(input_numbers, operation):
    key = int(input_numbers[0])
    numbers = [int(x) for x in input_numbers[1:]]

    encrypted_numbers = []
    for num in numbers:
        if operation == '+':
            encrypted_numbers.append(str(num + key))
        elif operation == '*':
            encrypted_numbers.append(str(num * key))
        elif operation == 'XOR':
            encrypted_numbers.append(str(num ^ key))
        else:
            return "Operate invalida. Te rog alege dintre +, *, sau XOR."

    return ' '.join(encrypted_numbers)


input_numbers = input("Introdu o lista de numere de forma 'xy' separate prin spatii: ").split()
operation = input("Alege o operatie (+, *, XOR): ")

result = encrypt_list(input_numbers, operation)
print(result)


# 12 23 54 12 38 76 34 21