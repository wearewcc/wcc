# Version A: Linear path
meal_price = float(raw_input('How much was your meal? '))
tip = meal_price * .20
total_price = meal_price + tip

print('You should tip $' + str(tip))
print('Your total cost would be $' + str(total_price))


# Version B: Conditional path
meal_price = float(raw_input('How much was your meal? '))
print('How was the service? ')
print('a. Not so good')
print('b. Good')
print('c. Excellent!')
service = raw_input('Choose an option: ')

if service == 1:
    percentage = .15;
elif service == 2:
    percentage = .18;
elif service == 3:
    percentage = .20;

tip = meal_price * .18
total_price = meal_price + tip
print('You should tip $' + str(tip))
print('Your total cost would be $' + str(total_price))
