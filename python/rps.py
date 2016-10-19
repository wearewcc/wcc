import random



def check_move(move):

    if move == 'rock' or move == 'paper' or move == 'scissors':
        return True
    else:
        return False


# Alternative version for check_move; just FYI:
def check_move2(move):
    return move == 'rock' or move == 'paper' or move == 'scissors':

# print check_move('rock') # Expect: True
# print check_move('paper') # Expect: True
# print check_move('scissors') # Expect: True
# print check_move('roc') # Expect False




def get_player_move():

    move = raw_input('Pick your move: rock, paper, or scissors? ')

    while check_move(move) == False:
        print('Invalid move; pick again.')
        get_player_move()

    return move

# print get_player_move()



def get_computer_move():
    moves = ['rock', 'paper', 'scissors'];
    return random.choice(moves)



def judge(moveA, moveB):

    # moveA is rock
    if moveA == 'rock' and moveB == 'paper':
        return False

    if moveA == 'rock' and moveB == 'scissors':
        return True

    # moveA is paper
    if moveA == 'paper' and moveB == 'rock':
        return True

    if moveA == 'paper' and moveB == 'scissors':
        return False

    # moveA is scissors
    if moveA == 'scissors' and moveB == 'rock':
        return False

    if moveA == 'scissors' and moveB == 'paper':
        return True


# print judge('rock','paper') # Expected: False
# print judge('rock','scissors') # Expected: True
# print judge('paper','rock') # Expected: True
# print judge('paper','scissors') # Expected: False
# print judge('scissors','rock') # Expected: True
# print judge('scissors','paper') # Expected: False



def play():

    print('Welcome to Rock, Paper, Scissors!')

    # Player goes
    player = get_player_move()

    # Computer goes
    computer = get_computer_move()
    print('The computer picked: ' + computer)

    # Report results
    if player == computer:
        print('Tie!')
    elif(judge(player, computer) == True):
        print('You won!')
    else:
        print('The computer won!')

    # Prompt to play again
    play_again = raw_input('Play again? Type `y` or `n`: ')

    if(play_again == 'y'):
        play()
    else:
        print('Thanks for playing!')


play()
