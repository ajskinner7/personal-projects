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
def drawnames(c):
    quartet = []
    for i in chorus.keys():
        quartet.append(chorus[i][randrange(len(chorus[i]))])
    print(quartet)

# run the program
print('--------16 Chairs--------\n')

chorus = asknames(chorus)
print(chorus)   
input('Press enter to generate a random quartet')

while True:
    drawnames(chorus)
    input('Press enter to generate another quartet.')
    
