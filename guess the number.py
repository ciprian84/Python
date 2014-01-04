# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console



import random
import simplegui
# initialize global variables used in your code
comp_number = 0
remaining_guesses = 0
msgRemGuesses = 'Number of remaining guesses is ' 

# define event handlers for control panel

def init():
  range100()  
   
def range100():
    # button that changes range to range [0,100) and restarts
    global comp_number
    global remaining_guesses
    #clear the input when a new game starts
    input.set_text("")
    remaining_guesses = 7
    comp_number =  random.randrange(0,100)
    print 'New game. Range is from 0 to 100.' + '\n' + msgRemGuesses + str(remaining_guesses) + '\n' 

def range1000():
    # button that changes range to range [0,1000) and restarts
    global comp_number 
    global remaining_guesses
    input.set_text("")
    remaining_guesses = 10
    comp_number = random.randrange(0, 1000)
    print 'New game. Range is from 0 to 1000.' + '\n' + msgRemGuesses + str(remaining_guesses) + '\n'
    
    
def get_input(guess):
    # main game logic goes here	
    global remaining_guesses
    print 'Guess was ' + str(guess)
    if int(guess) < comp_number:
        remaining_guesses = remaining_guesses - 1
        print msgRemGuesses + str(remaining_guesses)
        if remaining_guesses == 0:
            print 'You ran out of guesses. The number was ' + str(comp_number) + '\n'
            init()
        else:
            print 'Higher!' + '\n'
    elif int(guess) > comp_number:
        remaining_guesses = remaining_guesses - 1
        print msgRemGuesses + str(remaining_guesses)
        if remaining_guesses == 0:
            print 'You ran out of guesses. The number was ' + str(comp_number) + '\n'
            init()
        else:
            print 'Lower!' + '\n'
    #elif int(guess) == comp_number:
    else:
        remaining_guesses = remaining_guesses - 1
        print msgRemGuesses + str(remaining_guesses)
        print 'Correct!' + '\n'
        init()
 
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)
btnRange100 = frame.add_button('Range is [0, 100)', range100, 200)
btnRange1000 = frame.add_button('Range is [0, 1000)', range1000, 200)
input = frame.add_input('Enter a guess', get_input, 200)
# register event handlers for control elements

init()
# start frame
frame.start()

