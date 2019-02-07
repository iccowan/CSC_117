# Ian Cowan
# Feb 11 2019
# Problem 3 on page 115
# Age Classifier

# Prompts the user for their age
age = int(input('What is your age? '))

# Determines the user's age classification
if(age >= 0 and age <= 1):
    print('Wow I\'m not sure how you\'re doing this because you are an infant!')
elif(age > 1 and age < 13):
    print('You are a child.')
elif(age >= 13 and age < 20):
    print('You are a teenager.')
elif(age >= 20):
    print('You are an adult!')
else:
    print('Whoops, something went wrong. That age isn\'t valid!')
