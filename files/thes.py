import random  # Enable random functions from python library


def exiting():
    f.close()
    exit()


f = open('files/2of12id(rev).txt', 'rt')  # Open dictionary text file for reading

a,c,i,n,p,s,v = [],[],[],[],[],[],[]  # Empty lists for parts of speech
posList = [a,c,i,n,p,s,v]  # Meta-list of all part-of-speech lists
textLabels = ['A:', 'C:', 'I:', 'N:', 'P:', 'S:', 'V:']
varLabels = ['a', 'c', 'i', 'n', 'p', 's', 'v']
d1 = dict(zip(textLabels,posList))
d2 = dict(zip(varLabels,posList))
d3 = dict(zip(varLabels,textLabels))

for line in f:  # Loop through dictionary file, adding lines to pos lists
    for x1, y1 in d1.items():
        if x1 in line:
            y1.append(line)

i1 = input('Please enter a part of speech code: ')
if 'exit' in i1:
    exiting()
while str(i1) not in varLabels:
    i1 = input('Sorry, please try again: ')
else:
    i2 = input('Please enter a starting letter: ')
    if 'exit' in i2:
        exiting()
    while not i2.isalpha():
        i2 = input('Sorry, please try again: ')
    else:
        for x3, y3 in d3.values():
            if i1 = x3:
                if random.choice(x3)
            print(random.choice(x3))
