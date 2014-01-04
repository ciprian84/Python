# Rock-paper-scissors-lizard-Spock program

#  equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# convert number to a name
def number_to_name(number):
    # fill in your code below
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return 'No corresponding name for the specified number'
       
# convert name to number 
def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else :
        return -1   

def rpsls(name): 
    import random
    #set a flag for correct_number
    correct_number = False
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # compute difference of player_number and comp_number modulo five
    win = (comp_number - player_number) % 5

    print ''
    #if number is correct print the chooses, else print error messages
    if name_to_number(name) != -1:
        print "Player chooses " + number_to_name(player_number)
        print "Computer chooses " + number_to_name(comp_number)
    else:
        print "No corresponding name"
  
    if (win == 1 or win == 2) and name_to_number(name) != -1:
        print "Computer wins!"
    elif (win == 0) and name_to_number(name) != -1:
        print "Player and computer tie!"
    elif (win == 3 or win == 4) and name_to_number(name) != -1:
        print "Player wins!"
    else:
        print "Correct the name and try again"
        
# test
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
rpsls("rock")
rpsls('tesa')