# Ian Cowan
# Lab Partner: Jake Pfaller
# CSC 117b Lab 29
# Main File

# Import packages
import matplotlib.pyplot as plt

# Define main()
def main():
    '''
    # Histogram
    myGraphValues = [20, 6, 2, 5, 9, 1]
    myGraphWidths = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    myGraphColors = ['r', '#FF6600', 'y', 'g', 'b', 'DarkViolet']
    myGraphLabels = ['Dragon', 'Greyhound', 'Badger', 'Possum', \
                     'Phoenix', 'Mongolian Wild Ass']

    x = range(0, len(myGraphLabels))
    plt.bar(x, myGraphValues, align='center', width=myGraphWidths, \
            color=myGraphColors)
    plt.title('Favorite Animals')
    plt.ylabel('Number of People')
    plt.xlabel('Animal')
    plt.xticks(x, myGraphLabels)
    plt.show()
    '''

    '''
    # Pie Chart
    myGraphValues = [20, 6, 2, 5, 9, 1]
    myGraphColors = ['r', '#FF6600', 'y', 'g', 'b', 'DarkViolet']
    myGraphLabels = ['Dragon', 'Greyhound', 'Badger', 'Possum', \
                     'Phoenix', 'Mongolian Wild Ass']
    explode = (0, 0.2, 0, 0, 0, 0)
    plt.pie(myGraphValues, colors=myGraphColors, labels=myGraphLabels, \
            explode=explode, autopct='%1.1f%%', counterclock=False, \
            shadow=True)
    plt.title('Favorite Animals')
    plt.show()
    '''

    # Line Graph
    myGraphValues = [20, 6, 2, 5, 9, 1]
    myOtherGraphValues = [5, 6, 9, 22, 3, 4]
    plt.plot(range(len(myGraphValues)), myGraphValues, 's:')
    plt.plot(range(len(myOtherGraphValues)), myOtherGraphValues)
    plt.title('Temperatures')
    plt.grid()
    plt.legend(['mice', 'dragons'], loc=1)
    plt.savefig('MySampleImage.png', format='png')
    plt.show()

# Call main()
main()
