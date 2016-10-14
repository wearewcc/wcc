print('Welcome to the Mad Lib Generator!' + '\n')

first_adjective = raw_input('Type in an adjective:')
second_adjective = raw_input('Another adjective:')
third_adjective = raw_input('And another adjective:')
fourth_adjective = raw_input('One more adjective:')
animal = raw_input('Plural animal (e.g. puppies):')
verb = raw_input('Now a verb:')
noun = raw_input('Now a plural noun:')
musician = raw_input('The first name of a woman musician:')
beverage = raw_input('A beverage:')
body_part= raw_input('And finally, a plural body part:')
print('\n')
print("Excellent choices! Here's your story . . .")
print('----------------------------------' + '\n')

print('There once was a ' + str(first_adjective) + ' programmer named ' + str(musician))
print('who wanted to build a ' + str(second_adjective) + ' mobile app to')
print('help ' + str(third_adjective) + ' ' + str(animal) + ' find new homes.' + '\n')

print(str(musician) + ' stayed up all night, drinking lots of')
print('caffeinated ' + str(beverage) + ' as she worked and worked')
print('trying to complete her fancy program.' + '\n')

print('Whenever ' + str(musician) + ' hit a dead end, she would')
print('exclaim ' + '*' + str(noun) + '*' + '!' + '\n')

print('But she was not discouraged, and after a quick break')
print('to ' + str(verb) + ' and clear her head, she got back to work.' + '\n')

print('By morning, when the sun started to rise, she let out a')
print('big yawn and stretched her ' + str(body_part) + '.')
print('Finally, she was done.')
print('----------------------------------')
