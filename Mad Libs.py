import re

#Regular expression objects to search for
adjectiveRegex = re.compile(r'ADJECTIVE')
nounRegex = re.compile(r'NOUN')
nounsRegex = re.compile(r'NOUNS')
adverbRegex = re.compile(r'ADVERB')
verbRegex = re.compile(r'VERB')
nameRegex = re.compile(r'NAME')
verbWithIngRegex = re.compile(r'VERBING')
placeRegex = re.compile(r'PLACE')
timeRegex = re.compile(r'TIME')

#Open the mad libs text
MadLibFile = open('MadLibs.txt')


MadLibString = MadLibFile.readlines()

MadLibFile.close()

newMadLibString = list()

#This loop examines each line stored in 'MadLibString'
for item in MadLibString:

    #If no matches are found, then add the line to 'newMadLibString'
    nomatches = True

    #While this is true, keep looking for Regex objects
    keepWorkingOnString = True

    #Holds the edited line
    newString = item

    while keepWorkingOnString:

        if re.search(r'ADJECTIVE', newString):
            userVal = input("Enter an adjective\n")
            newString = adjectiveRegex.sub(userVal, newString, 1)
            nomatches = False

        if re.search(r'TIME', newString):
            userVal = input("Enter an unit of time\n")
            newString = timeRegex.sub(userVal, newString, 1)
            nomatches = False
        
        if re.search(r'PLACE', newString):
            userVal = input("Enter a place\n")
            newString = placeRegex.sub(userVal, newString, 1)
            nomatches = False

        if re.search(r'NOUNS', newString):
            userVal = input("Enter a plural noun\n")
            newString = nounsRegex.sub(userVal, newString, 1)
            nomatches = False
        
        if re.search(r'NOUN', newString):
            userVal = input("Enter a noun\n")
            newString = nounRegex.sub(userVal, newString, 1)
            nomatches = False

        if re.search(r'ADVERB', newString):
            userVal = input("Enter an adverb\n")
            newString = adverbRegex.sub(userVal, newString, 1)
            nomatches = False

        if re.search(r'VERBING', newString):
            userVal = input("Enter a verb ending in ing\n")
            newString = verbWithIngRegex.sub(userVal, newString, 1)
            nomatches = False
        
        if re.search(r'VERB', newString):
            userVal = input("Enter a verb\n")
            newString = verbRegex.sub(userVal, newString, 1)
            nomatches = False

        if re.search(r'NAME', newString):
            userVal = input("Enter a name\n")
            newString = nameRegex.sub(userVal, newString, 1)
            nomatches = False

        if nomatches:
            newMadLibString.append(newString)
            keepWorkingOnString = False;

        nomatches = True
        
#Create a new file for the completed MadLib
MadLibFile = open('MadLibsNew.txt', 'w+')

displayStory = ''

#Create a string to display the completed story to the user
for item in newMadLibString:
    MadLibFile.write(item)
    displayStory += item

print(displayStory)
    

MadLibFile.close()

garbage = input('Press enter to end program:')
