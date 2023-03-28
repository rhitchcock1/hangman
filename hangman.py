import random 
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
      word_completion = "_" + len(word)
      guessed = False
      guessed_letters = []
      guessed_words = []
      tries = 6
      print("Let's play CLI Hangman!")
      print(display_hangman(tries))
      print(word_completion)
      print("\n")
      while not guessed and tries > 0:
         guess = input("Guess a letter or word:").upper()
         if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Yas Queen!", guess, "is in the word.")        
         elif len(guess) == len(word) and guess.isalpha():

         else: 
             print("Not a valid guess.") 
         print(display_hangman(tries))
         print(word_completion)
         print("\n")            



   

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]




if __name__ == "__main__":
    main()