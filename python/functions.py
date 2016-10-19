def multiply(a, b):
    result = a * b
    return result

#solution = multiply(4, 5)
#print(solution) # Expected result: 20


def isPositive(a):
    if a > 0:
        return True
    else:
        return False

print(isPositive(-4)) # Expected: False
print(isPositive(4)) # Expected: True
print(isPositive(-9.9)) # Expected: False
print(isPositive(9.9)) # Expected: True


def cube(a):
    product = a * a * a
return product

def mystery(x,y,z):

    return x + (y * z)

print mystery('Hello', 3, '!') # Expected: 'Hello!!!'
print mystery('Goodbye', 2, '#') # Expected: 'Goodbye@@'

#
#
# print(multiply(-1, 55)) # 55
# print(multiply(3, 'Hello')) # 'HelloHelloHello'
# print(multiply(-3, 'Hello')) # (nothing, blank space)
#
#
#
# def display_winner(winner, msg):
#     print(winner + ' Won!')
#     print(msg)
#
#
# display_winner('Computer', 'You busted')
# display_winner('Computer', 'You busted')
#
#
#
# if player_total > 21 and computer_total > 21:
#     print('Tie! (Both Player and Computer busted.)')
# elif player_total == computer_total:
#     print('Tie!')
# elif computer_total > 21:
#     print('You win! (Computer busted.)')
# elif player_total > 21:
#     print('Computer wins. (You busted.)')
# elif player_total > computer_total:
#     print('You win! (You were closest to 21.)')
# else:
#     print('Computer wins. (It was closest to 21.)')
