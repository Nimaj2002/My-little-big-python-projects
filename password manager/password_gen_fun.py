import random

symbols = ['!', '#', '$', '%', '&', '(', ')', '+', '*']


def keygen(total_letter):
    key = ""
    for letter in range(1, total_letter + 1):

        letter_type_chek = random.randint(1, 3)  # 1 for A o z , 2 for symbols , 3 for numbers

        if letter_type_chek == 1:
            capital_chek = random.randint(1, 2)
            if capital_chek == 1:
                random_alphabet_num = (random.randint(65, 91))  # from_A_to_Z
                key += chr(random_alphabet_num)
            else:
                random_alphabet_num = (random.randint(97, 123))  # from_a_to_z
                key += chr(random_alphabet_num)

        elif letter_type_chek == 2:
            random_symbol_num = random.randint(0, 8)  # Symbols
            key += symbols[random_symbol_num]

        else:
            random_number_num = (random.randint(48, 58))  # from_0_to_9
            key += chr(random_number_num)

    return key

