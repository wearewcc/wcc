import random



# Params: None
# Returns: Integer
#
def get_guess():

    # Get initial guess
    guess = raw_input('Enter your guess: ')

    # Assume its not valid, until its proven otherwise
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
print get_guess() # Expected: Keeps prompting until user enters a valid number
