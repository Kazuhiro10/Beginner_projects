from random import *

sample_words = "apple banana mandarine peach pineapple melon watermelon starfruit lemon orange lime"
word_list = sample_words.split(" ")
letters_permitted = "qwertyuiopñlkjhgfdsazxcvbnm"
print("")
print("GAME START")
print(" ")

selected_word = choice(word_list)
selected_word_length = len(selected_word)
selected_word_letter = list(selected_word)

guessing_board = list()
for i in range(selected_word_length) :
    guessing_board.append("_")

for i in range(selected_word_length) :
    print(guessing_board[i],end=" ") 
    
  
misses = 6
correct = 0
correct_cum = 0
used_letter = list()

while misses != 0 :
    print(" ")
    print(" ")
    guessed_letter = input("Enter a letter: ").lower()
    used_letter.append(guessed_letter)
    print(" ")
    if len(guessed_letter) > 1 :
        misses -= 1
        print("Invalid syntax, you have",misses,"chance(s) left")
        print("Letter(s)/Symbol(s) used:",used_letter)
        print(" ")
        for i in range(selected_word_length) :
            print(guessing_board[i],end=" ")
        
            
    elif guessed_letter in guessing_board :
        misses -= 1
        print("Invalid syntax, you have",misses,"chance(s) left")
        print("Letter(s)/Symbol(s) used:",used_letter)
        print(" ")
        for i in range(selected_word_length) :
            print(guessing_board[i],end=" ")
            
    elif guessed_letter not in letters_permitted :
        misses -= 1
        print("Invalid syntax, you have",misses,"chance(s) left")
        print("Letter(s)/Symbol(s) used:",used_letter)
        print(" ")
        for i in range(selected_word_length) :
            print(guessing_board[i],end=" ")
            
    else :    
        for i in range(selected_word_length) :
            if selected_word_letter[i] == guessed_letter:
                guessing_board[i] = guessed_letter
                correct += 1  
        
        if correct == 0:
            misses -= 1
            print("Wrong! You have ",misses,"chance(s) left")
        else :
            print("You had",correct,"letter(s) right")
        print("Letter(s)/Symbol(s) used:",used_letter)
        print("")
    
        for i in range(selected_word_length) :
            print(guessing_board[i],end=" ")
        
        correct_cum = correct_cum + correct
        correct = 0
        print(" ")
        
        if correct_cum == selected_word_length :
            print(" ")
            print("You won! The word was: ", selected_word)
            break
        
if correct_cum == selected_word_length :
    print(" ")
else : 
    print(" ")
    print("You have lost all your chances, you lost! The correct word was: ", selected_word)
    print(" ")
    
