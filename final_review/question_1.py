# Exam review question 1

def getStudents():
    file_in = open('students.txt', 'r')
    students = list()
    file_in.readline()

    for line in file_in:
        student = dict()
        line = line.strip()
        lineArray = line.split(',')

        student['lname'] = lineArray[0]
        student['fname'] = lineArray[1]
        student['class'] = lineArray[2]
        student['hometown'] = lineArray[3]
        student['birthMonth'] = lineArray[4]
        student['gender'] = lineArray[5]

        students.append(student)

    return students

def printResults(percents):
    print('CLASS   ', '% Male', '% Female', '% Other/NA', sep="\t")
    print('Freshman', percents['male_1'], percents['female_1'], percents['other_1'], sep="\t")
    print('Sophomre', percents['male_2'], percents['female_2'], percents['other_2'], sep="\t")
    print('Junior  ', percents['male_3'], percents['female_3'], percents['other_3'], sep="\t")
    print('Senior  ', percents['male_4'], percents['female_4'], percents['other_4'], sep="\t")

def main():
    # Get list of students
    allStudents = getStudents()

    # Loop through each student and see how many are each gender
    allCounts = {
        'male_1' : 0,
        'male_2' : 0,
        'male_3' : 0,
        'male_4' : 0,
        'female_1' : 0,
        'female_2' : 0,
        'female_3' : 0,
        'female_4' : 0,
        'other_1' : 0,
        'other_2' : 0,
        'other_3' : 0,
        'other_4' : 0,
    }

    total = 0

    for s in allStudents:
        g = s['gender']
        y = s['class']

        if y.upper() == 'FRESHMAN':
            year = 1
        elif y.upper() == 'SOPHOMORE':
            year = 2
        elif y.upper() == 'JUNIOR':
            year = 3
        elif y.upper() == 'SENIOR':
            year = 4

        if g.upper() == 'MALE':
            if year == 1:
                allCounts['male_1'] += 1
            elif year == 2:
                allCounts['male_2'] += 1
            elif year == 3:
                allCounts['male_3'] += 1
            elif year == 4:
                allCounts['male_4'] += 1
        elif g.upper() == 'FEMALE':
            if year == 1:
                allCounts['female_1'] += 1
            elif year == 2:
                allCounts['female_2'] += 1
            elif year == 3:
                allCounts['female_3'] += 1
            elif year == 4:
                allCounts['female_4'] += 1
        else:
            if year == 1:
                allCounts['other_1'] += 1
            elif year == 2:
                allCounts['other_2'] += 1
            elif year == 3:
                allCounts['other_3'] += 1
            elif year == 4:
                allCounts['other_4'] += 1

        total += 1

    percentTotals = {
        'male_1' : 0,
        'male_2' : 0,
        'male_3' : 0,
        'male_4' : 0,
        'female_1' : 0,
        'female_2' : 0,
        'female_3' : 0,
        'female_4' : 0,
        'other_1' : 0,
        'other_2' : 0,
        'other_3' : 0,
        'other_4' : 0,
    }

    if total > 0:
        for k in allCounts:
            percentTotals[k] = int((allCounts[k] / total) * 100)

    printResults(percentTotals)

main()
