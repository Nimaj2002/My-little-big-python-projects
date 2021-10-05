letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encoding(encoding_mode , text , shift_number):
    new_text = ""
    text = text.lower()
    length = len(letters)    
    
    if encoding_mode == "encrypt":
        for letter in text:
                new_letter_index = letters.index(letter) + shift_number
                if new_letter_index < length:
                    new_text += letters[new_letter_index]
                else:
                    new_text += letters[new_letter_index-26]
                         
        
    elif encoding_mode == "decrypt" :
        for letter in text:
                new_letter_index = letters.index(letter) - shift_number
                if new_letter_index > 0 :
                    new_text += letters[new_letter_index]
                else:
                    new_text += letters[new_letter_index]
    
    print(new_text)        
        
        
direction = input("Do you want to encrypt or decrypt?:\t")
main_text = input(f"Please input your to {direction}:\t")
shifting_num = int(input(f"Please input shifiting number to {direction}:\t"))

encoding(encoding_mode = direction, text = main_text, shift_number = shifting_num)