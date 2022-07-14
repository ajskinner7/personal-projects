#16 Chairs
#This program creates a random quartet out of a barbershop chorus.

from random import *

#create dictionary
chorus = {
    'tenor': [],
    'lead': [],
    'baritone': [],
    'bass': []
}

# function that asks for names and puts them into the section lists
def asknames(c):
    member = 'blank'
    for i in c.keys():
        while member != '':
            member = input('Type in the name of the next {part}. If there are no more, press enter.'.format(part = i))
            if member:
                #add name to sectionlist
                c[i].append(member)           
            else:
                member = 'blank'
                break
    return c

# function that selects a singer from each section to be in the quartet
def drawnames(c, q):
    for i in c.keys():
        chosen = c[i][randrange(len(c[i]))]
        q.append(chosen)
        c[i].remove(chosen)
    return c, q

# run the program
print('--------16 Chairs--------\n')

asknames(chorus)
print(chorus)   
input('Press enter to generate a random quartet')

while True:
    quartet = []
    drawnames(chorus, quartet)
    print(quartet)
    input('Press enter to generate another quartet.')
    
# To implement:
# reset button
# Make it look and read nicely, i.e. get plural tenses correct, no weird list formatting
# Import a chorus from an external file, be able to delete members
# Create GUI
# choose a singer to be in a quartet with other random singers
