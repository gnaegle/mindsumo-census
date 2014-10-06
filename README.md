MindSumo Challenge - Analyzing Census Data
===============

Solution to Capital One's "Use population data to identify promising markets" challenge on MindSumo, which can be viewed [here](https://www.mindsumo.com/contests/200). Unfortunately, I did not win or get recognized.

Using the Census dataset, this program ranks the top five cities with a population of at least 50,000 with the highest population growth between 2010-2012, the top five cities with a population of at least 50,000 with the fastest population shrinkage, and the top five states with with the highest growth across all its cities.

Usage
------
`python parseCensus.py [File name of CSV file]`

When no file argument is given, it looks for a file called "Metropolitan_Populations__2010-2012_.csv". If a file is passed into the script, then it needs to be in the same format as the Metropolitan_Populations__2010-2012_.csv file in this repository.

