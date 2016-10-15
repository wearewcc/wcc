# name = raw_input('What is your name? ')
# print('Hi ' + name)


#
# age = raw_input('How old are you? ')
# dogYears = age * 7
# print('You are ' + dogYears + ' years old in dog years.')

# age = raw_input('How old are you? ')
# dogYears = int(age) * 7
# print('You are ' + str(dogYears) + ' years old in dog years.')



meal_price = float(raw_input('How much was your meal? '))
tip = meal_price * .20
total_price = meal_price + tip

print('You should tip $' + str(tip))
print('Your total cost would be $' + str(total_price))
