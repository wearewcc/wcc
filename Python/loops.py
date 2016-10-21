counter = 1
while counter <= 10:
    print '#' * counter
    counter = counter + 1


greeting = 'Hello World'
for letter in greeting:
    print letter


continents = ['Africa', 'Antarctica', 'Asia', 'Europe', 'North America', 'Australia', 'South America']
for continent in continents:
    print continent + ' is a continent.'

def print_vowels():
    vowels = 'aeiou'
    for letter in vowels:
        print letter
print_vowels()
