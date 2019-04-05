# Ian Cowan
# Apr 3 2019
# Problem 2 on page 416
# Capital Quiz

# Import Packages
import random

# Define getStates()
# Inputs:
#   NONE
# Outputs:
#   dict: states
def getStates():
    # Open the file_in
    file_in = open('states_caps.csv', 'r')

    # Skip first (title) line for csv
    file_in.readline()

    # Init states
    states = dict()

    # Loop through each line and add the specific information
    for line in file_in:
        line.strip()
        line = line.split(',')
        states[line[0]] = line[1]

    # Close file_in
    file_in.close()

    return states

# Define beginQuiz()
# Inputs:
#   dict: states
# Outputs:
#   NONE
def beginQuiz(states):
    # Init variables
    correct = 0
    total = 0
    quizOver = False

    # Put all keys into a list
    state_names = list(states.keys())

    # Print instructions
    print('You will be asked a random state and its capital until you have either:')
    print('- gone through all 50 states OR')
    print('- type "DONE" in the answer spot.')
    print('Your results will be graded and you will see your results at the end')
    input('Press enter to begin!')

    while (not quizOver) and len(state_names) > 0:
        # Choose a random state
        num_states_remain = len(state_names)
        if num_states_remain > 0:
            i = random.randint(0, num_states_remain - 1)
        else:
            i = 0
        this_state = state_names[i].upper()
        this_cap = states[state_names[i]].upper()

        # Ask the question
        ans = input('What is the capital of ' + this_state + '? ').upper()

        # Check the answer
        if ans == 'DONE':
            quizOver = True
        elif ans == this_cap:
            correct += 1
            total += 1
        else:
            total += 1

        # Remove the chosen state from the list
        del state_names[i]

    # Print results
    print('You got a total of', correct, 'capitals out of', total, 'capitals correct!')
    if total != 0:
        print('This is a score of', str('{:.2f}'.format((correct / total) * 100)) + '%')

# Define main()
def main():
    # Call getStates()
    states = getStates()

    # Call beginQuiz()
    beginQuiz(states)

# Call main()
main()
