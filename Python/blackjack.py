import random

# Set up
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
random.shuffle(cards)

# Round 1
player_card1 = cards.pop()
computer_card_1 = cards.pop()

print('Player card: ' + str(player_card1))
print('Computer card:  ' + str(computer_card_1))


# Round 2

decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')
if decision == 'h':
    player_card2 = cards.pop()
else:
    player_card2 = 0

computer_card_2 = cards.pop()


print('Player cards: ' + str(player_card1) + ', ' + str(player_card2))
print ('Computer cards: ' + str(computer_card_1) + ', ' + str(computer_card_2))



# Round 3

decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')
if decision == 'h':
    player_card3 = cards.pop()
else:
    player_card3 = 0

computer_total = computer_card_1 + computer_card_2
if computer_total <= '16':
    computer_card_3 = cards.pop()
else:
    computer_card_3 = 0


print('Player cards: ' + str(player_card1) + ', ' + str(player_card2) + ', ' + str(player_card3))
print('Computer cards: ' + str(computer_card_1) + ', ' + str(computer_card_2) + ', ' + str(computer_card_3))

#Results

player_final = player_card1 + player_card2 + player_card3
computer_final = computer_card_1 + computer_card_2 + computer_card_3

print('\nGame Over'+ '\nPlayer Total: ' + str(player_final) + '\nComputer total: ' + str(computer_final))

#Winner

if player_final > 21 and computer_final > 21:
    print('Tie! You both busted!')
elif player_final == computer_final and player_final <21 and computer_final <21:
    print ('Tie!!')
elif player_final <=21 and computer_final >21:
    print ('You Won!')
elif computer_final <= 21 and player_final <= 21 and player_final > computer_final:
    print('You Won!')
elif computer_final <= 21 and player_final <= 21 and computer_final > player_final:
    print('Computer Won!')
else:
    print('')
