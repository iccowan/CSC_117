# Ian Cowan
# Feb 11 2019
# Problem 2 on page 115
# Rectangle Length/Width Comparison

# Prompts the user for the length and width of both rectangles
len_a = float(input('What is the LENGTH of rectangle A? '))
wid_a = float(input('What is the WIDTH of rectangle A? '))
len_b = float(input('What is the LENGTH of rectangle B? '))
wid_b = float(input('What is the WIDTH of rectangle B? '))

# Carries out the appropiate calculations to find areas
area_a = len_a * wid_a
area_b = len_b * wid_b

# Decides which rectangle has the larger area
if(area_a > area_b):
    print('The area of rectangle A (' + str(area_a) + ') is LARGER THAN that of rectangle B (' + str(area_b) + ')!')
elif(area_b > area_a):
    print('The area of rectangle B (' + str(area_b) + ') is LARGER THAN that of rectangle A (' + str(area_a) + ')!')
elif(area_a == area_b):
    print('The area of rectangle A (' + str(area_a) + ') is EQUAL TO that of rectangle B (' + str(area_b) + ')!')
else:
    print('Whoops, something went wrong! For some reason your rectangles couldn\'t be calculated!')
