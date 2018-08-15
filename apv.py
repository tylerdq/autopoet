import random  # Enable random functions from python library


def exiting():
    f.close()
    exit()


f = open('2of12id(rev).txt', 'rt')  # Open dictionary text file for reading

a,c,i,n,p,s,v = [],[],[],[],[],[],[]  # Empty lists for parts of speech
posList = [a,c,i,n,p,s,v]  # Meta-list of all part-of-speech lists
textLabels = ['A:', 'C:', 'I:', 'N:', 'P:', 'S:', 'V:']
varLabels = ['a', 'c', 'i', 'n', 'p', 's', 'v']
d1 = dict(zip(textLabels,posList))
d2 = dict(zip(varLabels,posList))

for line in f:  # Loop through dictionary file, adding lines to pos lists
    for x1, y1 in d1.items():
        if x1 in line:
            y1.append(line)

i = input('Please choose between "form" or "rand": ')
if 'exit' in i:
    exiting()
else:
    while (i != 'form') and (i != 'rand'):
        if 'exit' in i:
            exiting()
        else:
            i = input('Sorry, please try again: ')

if i == 'form':  # Code block for "form" subprogram
    while True:
        i = input('Please enter desired format: ')
        if 'exit' in i:
            exiting()
        else:
            for letters in i:
                if 'exit' in i:
                    exiting()
                elif any(z in letters for z in d2.keys()):
                    for x2, y2 in d2.items():
                        if x2 in letters:
                            print(random.choice(y2))
                elif 'x' in letters:
                    print(random.choice(random.choice(posList)))
                else:
                    print('INVALID CHARACTER')

elif i == 'rand':  # Code block for "rand" subprogram
    while True:
        try:
            i = input('Please enter a numerical format length: ')
            if 'exit' in i:
                exiting()
            else:
                i = int(i)
        except ValueError:
                print('Please enter the value as an integer.')
                continue
        else:
            for number in range(i):
                print(random.choice(random.choice(posList)))

exiting()
