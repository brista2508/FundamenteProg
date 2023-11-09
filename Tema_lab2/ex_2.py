def count_symmetric_pairs(numbers):
    symmetric_count = 0
    n = len(numbers)

    for i in range(n):
        for j in range(i + 1, n):
            is_symmetric = True
            for k in range(len(numbers[i])):
                if numbers[i][k] != numbers[j][len(numbers[i]) - k - 1]:
                    is_symmetric = False
                    break

            if is_symmetric:
                symmetric_count += 1

    return symmetric_count

input_numbers = input("Introdu o lista de numere de forma 'xy' separate prin spatii: ").split()
symmetric_count = count_symmetric_pairs(input_numbers)
print("Numarul de perechi simetrice (xy si yx) este:", symmetric_count)


# 12 23 54 12 38 76 34 21