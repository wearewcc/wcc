print('Welcome to the Mad Lib Generator!\n')

# Ask the user for 10 unique words:
adjective1 = raw_input('Type in an adjective: ')
adjective2 = raw_input('Another adjective: ')
adjective3 = raw_input('And another adjective: ')
adjective4 = raw_input('One more adjective: ')

pluralAnimal = raw_input('Plural animal (e.g. puppies): ')
verb = raw_input('Now a verb: ')
pluralNoun = raw_input('Now a plural noun: ')

name = raw_input('The first name of a woman musician: ')
beverage = raw_input('A beverage: ')
pluralBodyPart = raw_input('And finally, a plural body part: ')

# When testing, uncomment these lines:
# adjective1 = 'fearless'
# adjective2 = 'gooey'
# adjective3 = 'sassy'
# adjective4 = 'fancy'
#
# pluralAnimal = 'elephants'
# verb = 'skip'
# pluralNoun = 'marbles'
#
# name = 'Ani'
# beverage = 'chocolate milk'
# pluralBodyPart = 'knees'

# Concatenate the given words into the following story
print("\nExcellent choices! Here's your story...")
print("--------------------------------")
print("There once was a " + adjective1 + " programmer named " + name)
print("who wanted to build a " + adjective2 + " mobile app to ")
print("help " + adjective3 + " " + pluralAnimal + " find new homes.")
print("")
print(name + " stayed up all night, drinking lots of ")
print("caffeinated " + beverage + " as she worked and worked")
print("trying to complete her " + adjective4 + " program.")
print("")
print("Whenever " + name + " hit a dead end, she would")
print("exclaim *" + pluralNoun + "*!")
print("")
print("But she was not discouraged, and after a quick break ")
print("to " + verb + " and clear her head, she got back to work.")
print("")
print("By morning, when the sun started to rise, she let out a")
print("big yawn and stretched her " + pluralBodyPart + ".")
print("Finally, she was done. ")
print("--------------------------------")


print("\nExcellent choices! Here's your story...")
print("--------------------------------")
print("There once was a " + adjective1 + " programmer named " + name)
print("who wanted to build a ___ mobile app to ")
print("help ___ ___ find new homes.")
print("")
print("___ stayed up all night, drinking lots of ___")
print("caffeinated ___ as she worked and worked")
print("trying to complete her ___ program.")
print("")
print("Whenever ___ hit a dead end, she would")
print("exclaim *___*!")
print("")
print("But she was not discouraged, and after a quick break ")
print("to ___ and clear her head, she got back to work.")
print("")
print("By morning, when the sun started to rise, she let out a")
print("big yawn and stretched her ___.")
print("Finally, she was done. ")
print("--------------------------------")
