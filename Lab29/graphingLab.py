# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Lab29 Graphing
# Main File

# Import Packages
import matplotlib.pyplot as plt

# Define main()
def main():
    # Line Plot
    # Get the primes
    f_in = open('linedata.txt', 'r')
    primes = list()
    for line in f_in:
        line = line.strip()
        primes.append(int(line))

    f_in.close()

    # Plot the primes
    plt.plot(range(1, len(primes) + 1), primes)
    plt.title('First 75 Primes in Intervals of 5')
    plt.xlabel('Prime Number')
    plt.ylabel('Value')
    plt.grid()
    plt.show()

    # Bar Graph
    # Get the primes
    f_in = open('bardata.txt', 'r')
    primes = list()
    for line in f_in:
        line = line.strip()
        primes.append(int(line))

    f_in.close()

    # Create a dictionary of the number of primes within each
    # hundreth (i.e. 100's, 200's, 300's, etc.)
    primeClassification = dict()
    for p in primes:
        d1 = str(p)[0]
        if int(d1) not in primeClassification:
            primeClassification[int(d1)] = 1
        else:
            primeClassification[int(d1)] += 1

    # Turn the dictionary into a list for ordering
    primeClass = list()
    for i in range(1, 10):
        primeClass.append(primeClassification[i])

    # Draw the bar graph
    plt.figure()
    xValues = [100, 200, 300, 400, 500, 600, 700, 800, 900]
    plt.bar(range(9), primeClass, align='center', \
            width=[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
    plt.title('Number of Primes in Each Hundreth')
    plt.ylabel('Number of Primes')
    plt.xlabel('Hundreth')
    plt.xticks(range(9), xValues)
    plt.show()

    # Pie Chart
    # Get the pilot distribution
    f_in = open('piedata.txt', 'r')
    pilotDist = dict()
    primes = list()
    for line in f_in:
        if line[0] != '#':
            line = line.strip()
            parts = line.split('=')
            singleTot = int(parts[1])
            pilotDist[parts[0]] = singleTot

    f_in.close()

    # Turn the data into a list for the graph
    labels = list()
    data = list()
    explode = list()
    for k in pilotDist:
        labels.append(k)
        data.append(pilotDist[k])
        if k == "Private Airplane":
            explode.append(0.1)
        else:
            explode.append(0)

    # Graph the data
    myGraphColors = ['r', '#FF6600', 'y', 'g', 'b', 'DarkViolet', 'DarkGray']
    plt.pie(data, colors=myGraphColors, labels=labels, autopct='%1.1f%%', \
            explode=explode, counterclock=False, shadow=True)
    plt.title('Percentage of Pilots Per Certification')
    plt.show()

# Call main()
main()
