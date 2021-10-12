import pandas

all_data = pandas.read_csv("nato_phonetic_alphabet.csv")
words_dic = {row.letter: row.code for key, row in all_data.iterrows()}


def NATO():
    try:
        user_word = input("Enter Your letter: ").upper()
        result = [words_dic[letter] for letter in user_word]
        print(result)
    except KeyError:
        print("Invalid input")
        NATO()


NATO()
