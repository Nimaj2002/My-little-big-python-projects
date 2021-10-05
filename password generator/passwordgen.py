import random

symbols = [ '!', '#', '$', '%', '&', '(', ')', '+', '*']

def keygen( total_letters , total_symbols , total_numbers ):
    key = ''
    
    while total_letters > 0 :
        
        letter_type_chek = random.randint(1,3)                        # 1 for A o z , 2 for symbols , 3 for numbers
        
        if letter_type_chek == 1:
            capital_chek = random.randint(1,2)
            if capital_chek == 1:
                random_alphabet_num = (random.randint(65,91))        #from_A_to_Z 
                key += chr(random_alphabet_num)
            else:
                random_alphabet_num = (random.randint(97,123))       #from_a_to_z 
                key += chr(random_alphabet_num)
            total_letters -= 1
            
        elif letter_type_chek == 2 and total_symbols > 0: 
            random_symbole_num = random.randint(0,8)                 #Symbols
            key += symbols[random_symbole_num] 
            total_symbols -= 1
            total_letters -= 1
        
        elif letter_type_chek == 3 and total_numbers > 0:
            random_number_num = (random.randint(48,58))              #from_0_to_9 
            key += chr(random_number_num)  
            total_numbers -= 1
            total_letters -= 1
        
        
    return key        
        

print("Welcome to Python key Generator")
total_letters = int(input("How many letters do you want to have in your password?:\t"))
total_symbols = int(input("How many symbols do you want to have in your password?:\t"))
total_numbers = int(input("How many numbers do you want to have in your password?:\t"))
print( keygen( total_letters , total_symbols , total_numbers ) )
input("Press Enter to exit")
