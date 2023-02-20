from turtle import *
import random

marker = Turtle()
scr = marker.getscreen()
marker.pensize(2)
marker.speed(0)
marker.ht()

global total_guesses

def main():
    #Initialize Game Board
    drawGallow()
    global total_guesses
    total_guesses = 0
    all_letters = [True] * 26
    drawAlphabet(all_letters)
    
    #Initialize Randomly Chosen Word
    possible_words = [['A','L','A','N',' ','T','U','R','I','N','G']
                      ,['D','O','N','A','L','D',' ','K','N','U','T','H']
                      ,['A','D','A',' ','L','O','V','E','L','A','C','E']
                      ,['G','R','A','C','E',' ','H','O','P','P','E','R']
                      ,['G','O','R','D','O','N',' ','M','O','O','R','E']]
    chosen_word = possible_words[random.randint(0,4)]

    #Colors for each Letter when printed. True = Green, False = Red
    guessed_word = [' '] * len(chosen_word)
    drawDashes(chosen_word)

    #Take in a users guess
    while total_guesses <= 6:
        

        if total_guesses == 6: #Lose
            loseGame(chosen_word)
            drawMan()
            break

        if guessed_word == chosen_word: #Win
            winGame()
            break
            
        guess = str(scr.textinput("Guess a letter: ", "Guess a letter: ")).upper()

        if guess not in chosen_word: #Wrong Guess
            all_letters[ord(guess) - 65] = False
            total_guesses += 1
            drawAlphabet(all_letters)
            drawMan()
        elif guess in chosen_word and all_letters[ord(guess) - 65] == True: #Correct Guess
            guessed_word = updateGuess(guess, chosen_word, guessed_word)
            drawGuess(guess, guessed_word)
            all_letters[ord(guess) - 65] = False
            drawAlphabet(all_letters)

def loseGame(chosen_word):
    marker.pu()
    marker.goto(-50,250)
    marker.color("red")
    word = ''.join(chosen_word)
    marker.write("You Lose! The correct answer was:\n" + word, True, font=("Arial",16,"bold"))

def winGame():
    marker.pu()
    marker.goto(-50,250)
    marker.color("green")
    marker.write("Congratulations you won!", True, font=("Arial",16,"bold"))

def drawGallow():
    marker.pu()
    marker.goto(-350,0)
    marker.pensize(3)
    marker.pd()
    marker.fd(150)
    marker.pu()
    marker.goto(-275,0)
    marker.seth(90)
    marker.pd()
    marker.fd(300)
    marker.seth(0)
    marker.fd(100)
    marker.seth(270)
    marker.fd(25)

def drawMan():
    marker.pu()
    marker.goto(0,0)
    marker.color("black")
    if total_guesses == 1: #Head
        marker.goto(-200,250)
        marker.pd()
        marker.circle(25)
    elif total_guesses == 2: #Body
        marker.goto(-200,225)
        marker.seth(0)
        marker.pd()
        marker.fd(50)
        marker.rt(90)
        marker.fd(75)
        marker.rt(90)
        marker.fd(50)
        marker.rt(90)
        marker.fd(75)
    elif total_guesses == 3: #Left Arm
        marker.goto(-200,200)
        marker.seth(90)
        marker.lt(35)
        marker.pd()
        marker.fd(55)
    elif total_guesses == 4: #Right Arm
        marker.goto(-150,200)
        marker.seth(90)
        marker.rt(35)
        marker.pd()
        marker.fd(55)
    elif total_guesses == 5: #Left Leg
        marker.goto(-200,150)
        marker.seth(270)
        marker.rt(15)
        marker.pd()
        marker.fd(75)
    elif total_guesses == 6: #Right Leg * Lost the Game!
        marker.goto(-150,150)
        marker.seth(270)
        marker.lt(15)
        marker.pd()
        marker.fd(75)

def drawAlphabet(all_letters):
    marker.pu()
    marker.goto(-300,-100)
    marker.color("black")
    marker.write("Letters:     ", True, font=("Arial",16,"bold"))

    for x in range(65,91):
        if all_letters[x - 65] == True:
            marker.color("green")
            marker.write(chr(x) + " ", True, font=("Arial",16,"normal"))
        else:
            marker.color("red")
            marker.write(chr(x) + " ", True, font=("Arial",16,"normal"))

def drawDashes(chosen_word):
    marker.pu()
    marker.goto(-50,0)
    marker.color("black")
    for x in chosen_word:
        if x != ' ':
            marker.write("_ ", True, font=("Courier New",24,"bold"))
        else:
            marker.write("  ", True, font=("Courier New",24,"bold"))
    
def drawGuess(guess, guessed_word):
    marker.pu()
    marker.goto(-50,10)
    marker.color("black")
    for x in range(0,len(guessed_word)):
        if x != ' ':
            marker.write(guessed_word[x] + " ", True, font=("Courier New",24,"normal"))
        else:
            marker.write("  ", True, font=("Courier New",24,"normal"))

def updateGuess(guess, chosen_word, guessed_word):
    for x in range(0,len(chosen_word)):
        if chosen_word[x] == guess:
            guessed_word[x] = chosen_word[x]
    return guessed_word

main()
