# Ian Cowan
# Mar 25 2019
# Problem 7 on page 335
# Driver's License Exam

# Define getApplicantAnswers()
# Inputs:
#   NONE
# Outputs:
#   list: s_answer
def getApplicantAnswers():
    # Open driver_test_ans.txt
    file_in = open('driver_test_ans.txt', 'r')

    # Init variables
    s_answer = list()

    # Loop through each answer and add it to a list
    for line in file_in:
        s_answer.append(line.rstrip('\n'))

    return s_answer

# Define compareAnswers()
# Inputs:
#   list: correct
#   list: given
# Outputs:
#   int: correct_num
#   int: incorrect
#   list: incorrect_ans
def compareAnswers(correct, given):
    # Init variables
    correct_num = 0
    incorrect = 0
    incorrect_ans = list()
    i = 0

    # Loop through each correct answer and compare the given answer
    for ans in correct:
        if ans == given[i]:
            # Correct!
            correct_num += 1
        else:
            # Incorrect
            incorrect += 1

            # Add its number to the list
            incorrect_ans.append(i + 1)

        i += 1

    return correct_num, incorrect, incorrect_ans

# Define passOrFail()
# Inputs:
#   int: num_c
# Outputs:
#   bool: passed
def passOrFail(num_c):
    # Check to see if they got more than 15 correct
    if num_c >= 15:
        passed = True
    else:
        passed = False

    return passed

# Define main()
def main():
    # Set the correct answers
    answer = ['A', 'C', 'A', 'A', 'D',\
              'B', 'C', 'A', 'C', 'B',\
              'A', 'D', 'C', 'A', 'D',\
              'C', 'B', 'B', 'D', 'A']

    # Call getApplicantAnswers
    applicant_ans = getApplicantAnswers()

    # Call compareAnswers()
    correct, incorrect, incorrect_ans = compareAnswers(answer, applicant_ans)

    # Call passOrFail()
    passTest = passOrFail(correct)

    # Return the information
    if passTest:
        print('The applicant successfully passed the test')
    else:
        print('The applicant did not successfully pass the test')

    print('Number of Correct Answers:', correct)
    print('Number of Incorrect Answers:', incorrect)

    # Loop through the wrong answers and print them
    print('Incorrect answers: ', end='')
    for a in incorrect_ans:
        print(a, end=' ')
    print('')


# Call main()
main()
