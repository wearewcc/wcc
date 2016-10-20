import random


# Params: None
# Returns: Integer
#
def get_guess():

    # Get initial guess
    guess = raw_input('Enter your guess: ')

    # Assume it's not valid, until it's proven otherwise
    valid = False

    while valid != True:

        try:
            # Try and convert this number to an integer
            # If it fails, the exception will occur
            guess = int(guess)
        except Exception:
            # Exception was thrown when trying to convert to number,
            # Report the issue and ask again
            print('Invalid input; please enter a whole number.')
            valid = False
            guess = get_guess()

        # If they get here, it means the number must have been valid
        # Set valid to be true to break out of the while loop
        valid = True

    return guess

# Test get_guess
# print get_guess() # Expected: Keeps prompting until user enters a valid number


# Params: Int numA, Int numB
# Returns: String 'high' or 'low'
def compare(numA, numB):

    if numA > numB:
        return 'high'
    else:
        return 'low'

# Test compare
#print compare(100,1)  # Expected: 'high'
#print compare(1,100)  # Expected: 'high'
#print compare(99,100) # Expected: 'low'


#
#
#
def play():

    # Pick a secret number
    secret_number = random.randint(1, 100)

    # When building your program, the following line will tell you what
    # the secret_number is; this will make it easier to test the game.
    # When done, remove or comment-out this line.
    print('Debugging -> The secret number is: ' + str(secret_number))

    # Prompt user for their guess
    print("\nI'm thinking of a number between 1 and 100; what do you think it is?")
    guess = get_guess()

    # Keep prompting until they get it
    while guess != secret_number:
        results = compare(guess, secret_number);
        print('Too ' + results + '. Guess again.\n')
        guess = get_guess()

    # Conclusion
    print('You got it! The number was ' + str(secret_number))

play()
