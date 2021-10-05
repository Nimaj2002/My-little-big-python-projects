letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(text , shift):           
    new_text = ""
    text = text.lower()
    length = len(letters)
    for letter in text:
            new_letter_index = letters.index(letter) + shift
            if new_letter_index < length:
                new_text += letters[new_letter_index]
            else:
                new_text += letters[new_letter_index-26]
                
    print(new_text)

encrypt("zulu",5)
