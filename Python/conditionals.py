
print('TEMPerature CONDitional')

#temp = int(raw_input('What is the temperature?'))

#print('You should bring the following items:')
if temp <= 40:
    print('Coat')
    print('Hat')
    print('Gloves')
elif temp <= 70:
    print('Coat')
    print('Hat')
else:
    print('Nothing!')

print ('chained conditional with one elif')

#age = int(raw_input('How old are you?'))
if age < 3:
    print('baby')
elif age < 18:
    print('child')
else:
    print('adult')

print('chained conditional with several elifs')
age = int(raw_input('How old are you?'))
if age < 3:
    print('baby')
elif age < 16:
    print('adolescent')
elif age < 18:
    print('child')
elif age < 21:
    print('young adult')
else:
    print('adult')

print('no elifs, so basically an either or')
age = int(raw_input('How old are you?'))
if age < 18
    print('child')
else:
    print('adult')

print('final else not needed')
age = int(raw_input('How old are you?'))
if age > 75:
    print('retired')

print('chained conditional')
age = int(raw_input('How old are you?'))

if age > 16:
    print('You can drive')
if age > 18:
    print('You can vote')
if age > 21:
    print('You can join the military')
if age > 75:
    print('You can retire')
