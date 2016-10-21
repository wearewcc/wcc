import random


# Get the user’s guess
# Params: None
# Returns: Integer
#
def get_guess():

    # Get initial guess
    guess = raw_input('Enter your guess: ')

    # Assume it’s not valid, until it’s proven otherwise
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

# this is the error it keeps giving me.
  File "guess_again_v1.py", line 4
SyntaxError: Non-ASCII character '\xe2' in file guess_again_v1.py on line 4, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
