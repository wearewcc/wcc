# Set up
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
random.shuffle(cards)


# Round 1
player_card = cards.pop()
computer_card = cards.pop()

if player_card > computer_card:
    player_cards.append(player_card, computer_card)
    player_won = True;
elif computer_card > player_card:
    computer_cards.append(player_card, computer_card)
    player_won = False;

print('Player: ' + str(player_card))
print('Computer: ' + str(computer_card))

if player_won:
    print('You win this round!')
else:
    print('Computer wins this round')
