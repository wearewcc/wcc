print round(3.1459, 2) == 3.15 # Expected: True


def addTogether(a, b):
    return a + b

#addTogether(9, 50)
#print addTogether(9, 50)


def getSeason(month):

    month = month.lower()

    winter = ['dec','jan','feb']
    spring = ['mar', 'apr', 'may']
    summer = ['jun', 'jul', 'aug']
    fall   = ['sep', 'oct', 'nov']

    if month in winter:
        return 'Winter'
    elif month in spring:
        return 'Spring'
    elif month in summer:
        return 'Summer'
    elif month in fall:
        return 'Fall'
    else:
        return 'Month not found'


# print getSeason('jan') # Expected: Winter
# print getSeason('Jan') # Expected: Winter
# print getSeason('may') # Expected: Spring
# print getSeason('aug') # Expected: Summer
# print getSeason('sep') # Expected: Fall
# print getSeason('augg') # Expected: Month not found


def getCelsius(temp):

    return (temp - 32) / 1.8

print getCelsius(55) # Expected: 12.7777777778


def getFahrenheit(temp):

    return (temp * 1.8) + 32

print getFahrenheit(10) # Expected: 50.0


def temperatureConverter(temp, scale):

    if scale == 'C':
        return getCelsius(temp)
    else:
        return getFahrenheit(temp)

print temperatureConverter(55, 'C') # 12.7777777778
print temperatureConverter(10, 'F') # 50.0



def temperatureConverterV2(temp, scale):

    if scale == 'C':
        return getCelsius(temp)
    elif scale == 'F':
        return getFahrenheit(temp)
    else:
        return "Error: Invalid temperature scale; Must be `F` or `C`"

print temperatureConverterV2(55, 'C') # 12.7777777778
print temperatureConverterV2(10, 'F') # 50.0
print temperatureConverterV2(55, 'X') # Error: Invalid temperature scale; Must be `F` or `C`

def vowelCounter(word):

    vowelCount = 0
    for letter in word:
        if letter in 'aeiou':
            vowelCount += 1

    return vowelCount


print vowelCounter('apples') # Expected: 2
print vowelCounter('aeiou') # Expected: 5
print vowelCounter('why') # Expected: 0
print vowelCounter('mississippi') # Expected: 4
