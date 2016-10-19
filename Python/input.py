#name = raw_input('What is your name? ')
#print('Hi ' + name)

#name = raw_input('What is your name?')
#age = raw_input('How old are you?')
#print(name + ' is ' + age + ' years old.')

#age = raw_input('How old are you?')
#dog_years = age * 7
#print('You are ' + dog_years + 'old in dog years.')


#age = raw_input('How old are you? ')
#dog_years = int(age) * 7
#print('You are ' + str(dog_years) + ' years old in dog years.')

#this was Kazia's original
#check = raw_input('How much was your meal?')
#tip_amount = float(check) * 0.2
#print('You should tip $' + str(tip_amount))
#print('Your total cost would be $' + str(float(check) + tip_amount))


#Ben's version: he couldn't resist Atom being open
#check = raw_input('How much was your meal?')
#percent = raw_input('what percent do you want to tip?')
#tip_amount = float(check) * (float(percent)/100)
#print('You should tip $' + str(tip_amount))
#print('Your total cost would be $' + str(float(check) + tip_amount))

#updated with conditionals now

meal_price = float(raw_input('How much was your meal? '))
print('How would you rate the service? ')
print('a. Not so good')
print('b. Good')
print('c. Excellent!')
chosen_option = raw_input('Choose an option: ')

# Here's where conditionals come in...
if chosen_option == 'a':
    percentage = .15;
elif chosen_option == 'b':
    percentage = .18;
elif chosen_option == 'c':
    percentage = .20;
else:
    percentage = .20
    print('You did not enter a valid option, defaulting to 20%')

tip = meal_price * percentage
total_price = meal_price + tip
print('You should tip $' + str(tip))
print('Your total cost would be $' + str(total_price))

if player1 == 'winner':
    print('Player 1 wins!')
elif player2 == 'winner':
    print('Player 2 wins!')
elif player3 == 'winner':
    print('Player 3 wins!')
