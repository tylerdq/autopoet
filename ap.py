import sys  # Enable passing command line arguments to script
import random  # Enable random functions from python library

f = open('2of12id(rev).txt', 'rt')  # Open dictionary text file for reading

if sys.argv[1] == 'help':
    print('autopoet usage:\n"python ap.py <subprogram> <option>"\nSubprograms include "form" and "rand"\nOptions include letters for "form" and integers for "rand"')
    f.close()
    exit()

elif len(sys.argv) == 3:
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

    if sys.argv[1] == 'form':  # Code block for "form" subprogram
        for letters in sys.argv[2]:
            if any(z in letters for z in d2.keys()):
                for x2, y2 in d2.items():
                    if x2 in letters:
                        print(random.choice(y2))
            elif 'x' in letters:
                print(random.choice(random.choice(posList)))
            else:
                print('INVALID CHARACTER')

    elif sys.argv[1] == 'rand':  # Code block for "rand" subprogram
        while True:
            try:
                sys.argv[2] = int(sys.argv[2])
            except ValueError:
                print('Please enter the value as an integer.')
                f.close()
                exit()
            else:
                for number in range(sys.argv[2]):
                    print(random.choice(random.choice(posList)))
                f.close()
                exit()

else:
    print('Incorrect input. Run "python ap.py help" for help.')

f.close()
exit()
