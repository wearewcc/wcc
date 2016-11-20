print('Boolean basics')

print(1 == 1) # Expected output: True

print(1 == 2) # Expected output: False

print(1 > 2) # Expected output: False

print(2 > 1) # Expected output: True

print(1 >= 1) # Expected output: True

print(2 == 2) # Expected output: True

print(2 != 2) # Expected output: False

print('predict Boolean outcome')

age = 30

print(age > 10) # Expected outcome: True

print(10 < age) # Expected outcome: True

print(age > 10 + 20) # Expected outcome: False

print(age + 20 > 10) # Expected outcome: True


print('a' > 'z') # Expected outcome: True

print('z' > 'a') # Expected outcome: False

print('apples' > 'oranges') # Expected outcome: True

print('oranges' > 'apples') # Expected outcome: False

print('cat' > 'car') # Expected outcome: False

print('car' > 'cat') # Expected outcome: True

print('logical operators')

age = 1
print(age > 12 and age < 19) # Expected outcome: False

age = 14
print(age > 12 and age < 19) # Expected outcome: True

age = 19
print(age > 12 and age < 19) # Expected outcome: False

age = 18
print(age > 12 and age < 19 and age != 5) # Expected outcome: True

age = 5
print(age > 12 and age < 19 and age != 5) # Expected outcome: False

age = -1
print(age > 12 and age < 19) # Expected outcome: False

age = 10
print(age > 25 and age < 15) # Expected outcome: False
# Could the above expression ever be True? I can't see it

print('rock paper scissors')

gesture = 'rock'
print(gesture == 'rock' or gesture == 'paper' or gesture == 'scissors') # Expected outcome: True

gesture = 'pape'
print(gesture == 'rock' or gesture == 'paper' or gesture == 'scissors') # Expected outcome: False

print ('Challenge questions')

gesture = 'rock'
print(gesture == 'rock' and gesture == 'paper' or gesture == 'scissors') # Expected outcome: False

age = int(raw_input('How old are you?'))
print(age > 4 and age <11) #expected outcome: True

age = int(raw_input('How old are you?'))
print(age >=5 and age <=10 ) #expected outcome: True

#when it said think of three ways, I thought it had to be 3 ways with only two constraints! I feel less dumb

age = int(raw_input('How old are you?'))
print(age > 5 and age <10)   #expected outcome: true

age = int(raw_input('How old are you?'))
print(age >= 6 and age <=9 )   #expected outcome: true
