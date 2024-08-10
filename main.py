import hangman_words
import random
import hangmam_art

# defining the function to replace the character in dashed word
def replace_char(s , position, char):
  return s[:position] + char + s[position +1 :]
  
# Logo of Game
print(hangmam_art.logo)
# getting a random word from hangman_word file
random_word = random.choice(hangman_words.word_list)
# generating dashes for the word selected 
dashed_text = random_word.replace(random_word,"-"*len(random_word))

lives = 7
print(dashed_text)
while True:
  # Asking user for guess
  user_guess = input("Guess a letter:").lower()
  if user_guess in random_word:
    # print(i)
    index = random_word.index(user_guess)
    dashed_text = replace_char(dashed_text, index, user_guess)
    print(dashed_text)
    if "-" in dashed_text:
      continue
    else:
      print("you have won!")
      break
  else:
    lives -= 1
    if lives == 6:
      print(hangmam_art.stages[6])
      print(f"lives left {lives}")
    elif lives == 5:
      print(hangmam_art.stages[5])
      print(f"lives left {lives}")
    elif lives == 4:
      print(hangmam_art.stages[4])
      print(f"lives left {lives}")
    elif lives == 3:
      print(hangmam_art.stages[3])
      print(f"lives left {lives}")
    elif lives == 2:
      print(hangmam_art.stages[2])
      print(f"lives left {lives}")
    elif lives == 1:
      print(hangmam_art.stages[1])
      print(f"lives left {lives}")
    else:
      print(hangmam_art.stages[0])
      print("Game Over. You lost !")
      break
  print(dashed_text)