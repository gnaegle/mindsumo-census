import csv
import sys

# Allowing passing of file name to the program or just uses the default file name if one is not provided
if(len(sys.argv) == 1):
    fileName = "Metropolitan_Populations__2010-2012_.csv"
elif(len(sys.argv) == 2):
    fileName = sys.argv[1]
else:
    print "Format for the program is: python parseCensus.py [File name of CSV file]"
    sys.exit(1)

# Attempting to open CSV and giving error if this fails
try:
    csvFile  = open(fileName, "rU")
except IOError:
    print fileName, "cannot be opened"
    sys.exit(1)

# Putting parsed contents of the CSV file into a variable    
csvReader = csv.reader(csvFile)

# Initializing dictionaries
cities = {}
statesBefore = {}
statesAfter = {}
statesResult = {}

firstRow = True;

# Iterating through city census data line-by-line
for row in csvReader:
    # Skipping first line because it is simply the headers for columns of data
    if firstRow:
        firstRow = False
        continue;
    
    # Parsing line into city, state, population in 2010, and population in 2012
    city, state = row[0].split(", ")
    before = int(row[1])
    after = int(row[3])
    
    # Populating dictionaries for each state
    if(not statesBefore.has_key(state)):
        statesBefore[state] = before
        statesAfter[state] = after
    else:
        statesBefore[state] += before
        statesAfter[state] += after
    
    # Populating dictionary for the cities
    if(before >= 50000):
        perc = (after - before) / float(before)
        cities[row[0]] = perc * 100

# Closing handle to CSV file       
csvFile.close()

# Putting the city data into sorted order to find the largest growth cities and the smallest growth cities
sortedGrowth = sorted(cities.iteritems(), key=lambda (k,v): (v,k))

# Calculating percentage growth for each state
for key in statesBefore.keys():
    statesResult[key] = ((statesAfter[key] - statesBefore[key]) / float(statesBefore[key])) * 100

# Putting the state data into sorted order to find the largest growth states
statesResult = sorted(statesResult.iteritems(), key=lambda (k,v): (v,k))

# Printing out 5 cities with largest growth
print "Highest population growth by city:"
for i in range(1, 6):
    print str(i) + ".", sortedGrowth[len(sortedGrowth) - i][0], "(" + str(sortedGrowth[len(sortedGrowth) - i][1]) + "%)"

# Printing out 5 cities with smallest growth    
print "\n"
print "Lowest population growth:"
for i in range(1, 6):
    print str(i) + ".", sortedGrowth[i][0], "(" + str(sortedGrowth[i][1]) + "%)"

# Printing out 5 states with largest growth
print "\n"
print "Highest population growth by state:"
for i in range(1, 6):
    print str(i) + ".", statesResult[len(statesResult) - i][0], "(" + str(statesResult[len(statesResult) - i][1]) + "%)"