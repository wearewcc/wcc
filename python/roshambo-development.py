import random


# Accepts: a String `move`
# Returns: Boolean for whether move is valid
#
# Valid moves include 'rock', 'paper', or 'scissors'`
#
def check_move(move):

    return ''


# Test the check_move function
print check_move('rock') # Expect: True
print check_move('paper') # Expect: True
print check_move('scissors') # Expect: True
print check_move('roc') # Expect False



# Accepts: Nothing
# Returns: String of 'rock', 'paper', or scissors'
# Prompts the user for a move
# Makes sure that move is valid; if it's not, continues to ask user for a move
def get_player_move():

    move = raw_input('Pick your move: rock, paper, or scissors? ')

    while check_move(move) == False:
        print('Invalid move; pick again.')
        get_player_move()

    return move

print get_player_move()
# Test with: rock, paper, scissors, roc, 1



# Accepts: Nothing
# Returns: String of 'rock', 'paper', or 'scissors'
def get_computer_move():
    moves = ['rock', 'paper', 'scissors'];
    return random.choice(moves)


# Accepts: String moveA, String moveB
# Returns: Boolean if moveA beats moveB according to the rules of Roshambo
#
# Examples:
# If moveA is 'rock' and moveB is 'paper', it should return False
# If moveA is 'paper' and moveB is 'rock', it should return True
#
# Should work for 6 different posssible combinations of moveA and moveB
def judge(moveA, moveB):

    pass


# print judge('rock','paper') # Expected: False
# print judge('rock','scissors') # Expected: True
# print judge('paper','rock') # Expected: True
# print judge('paper','scissors') # Expected: False
# print judge('scissors','rock') # Expected: True
# print judge('scissors','paper') # Expected: False



def play():

    print('Welcome to Roshambo!')

    player = get_player_move()

    computer = get_computer_move()
    print('The computer chose ' + computer)

    didPlayerWin = compare_moves(player, computer)

    if(didPlayerWin == True):
        print('You won!')
    else:
        print('The computer won!')

    play_again = raw_input('Play again? Type `y` or `n`: ')

    if(play_again == 'y'):
        play()
    else:
        print('Thanks for playing!')


#play()
