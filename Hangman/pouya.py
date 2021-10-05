import random

word_list = ["lion", "tiger", "snake", "bear", "wolf", "shark", "dolphin", "dog", "cat", "ant", "cow", "donkey", "butterfly", "eagle", "fox"]

correct_word = random.choice(word_list)

guessed_now = []
correct_word_inlist = []

for letter in range(len(correct_word)):
  guessed_now.append("_")

for letter in correct_word:
  correct_word_inlist += letter
  

print(guessed_now)

tries = 0

play = True
lose = False
while play:
  guess = input("guess a letter: ").lower()

  def check_letter(letter, is_correct):
    global tries
    for position in range(len(correct_word)):
      if letter == correct_word[position]:
        guessed_now[position] = correct_word[position]
        is_correct = True
    if not is_correct:
      tries +=1
      
  check_letter(guess, False)
  print(guessed_now)
  if tries == 7:
    lose = True
    play = False
  if guessed_now == correct_word_inlist:
    play = False
  if tries < 7:  
    print(f"you have {7-tries} tries left")

if lose:
  print(f"you lost! The animal was {correct_word}.")
else:
  print("you win")
