if 0:
    print '#'
    print '##'
    print '###'
    print '####'
    print '#####'
    print '######'
    print '#######'
    print '########'
    print '#########'
    print '##########'

if 0:
    print '#' * 1
    print '#' * 2
    print '#' * 3
    print '#' * 4
    print '#' * 5
    print '#' * 6
    print '#' * 7
    print '#' * 8
    print '#' * 9
    print '#' * 10

if 0:
    counter = 1
    while counter <= 10:
        print '#' * counter
        counter = counter + 1


if 0:
    numbers = range(0,10) # Produces a list like [0,1,2,3,4,5,6,7,9]
    for counter in numbers:
        print counter * '#'


if 0:
    greeting = 'Hello World'
    for letter in greeting:
        print letter


if 0:
    continents = ['Africa', 'Antarctica', 'Asia', 'Europe', 'North America', 'Australia', 'South America']
    for continent in continents:
        print continent + ' is a continent.'


if 0:
    # One approach:
    def print_vowels():

        vowels = ['a','e','i','o','u']

        for letter in vowels:
            print letter


    # This also works:
    def print_vowels():

        vowels = 'aeiou'

        for letter in vowels:
            print letter

    print_vowels()



if 1:
    def print_vowels_v2():

        vowels = ['a','e','i','o','u']

        counter = 0

        while counter < 5:
            print vowels[counter]
            counter += 1

    print_vowels_v2()
