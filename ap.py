import sys  # Enable passing command line arguments to script
import random  # Enable random functions from python library
import string  # Enable listing of ASCII characters

f = open('words.txt', 'rt')  # Open dictionary text file for reading

if len(sys.argv) == 1:
    print('Incomplete input. Run "python ap.py help".')
    f.close()
    exit()

elif len(sys.argv) == 2:
    if sys.argv[1] == 'help':
        print('\n"python ap.py <subprogram> <arg1> <arg2>"\n\n    Subprogram: "form", "rand", or "thes"\n    arg1:\n        - "form": Any arbitrary combination of [a,c,i,n,p,s,v,x]\n        - "rand": Any positive integer\n        - "thes": Any one of [a,c,i,n,p,s,v]\n    arg2:\n        - "thes": Any lowercase letter from a-z\n')
        f.close()
        exit()
    else:
        print('Incomplete input. Run "python ap.py help".')
        f.close()
        exit()

elif len(sys.argv) >= 3:
    a,c,i,n,p,s,v = [],[],[],[],[],[],[]  # Empty lists for parts of speech
    posList = [a,c,i,n,p,s,v]  # Meta-list of all part-of-speech lists
    textLabels = ['A:', 'C:', 'I:', 'N:', 'P:', 'S:', 'V:']
    varLabels = ['a', 'c', 'i', 'n', 'p', 's', 'v']
    alphas = list(string.ascii_lowercase)  # List of all lc alpha characters
    selectWords = []
    d1 = dict(zip(textLabels,posList))
    d2 = dict(zip(varLabels,posList))

    for line in f:  # Loop through dictionary file, adding lines to pos lists
        for x1, y1 in d1.items():
            if x1 in line:
                y1.append(line.strip())

    if sys.argv[1] == 'form':  # Code block for "form" subprogram
        print()
        for letters in sys.argv[2]:
            if any(z in letters for z in d2.keys()):
                for x2, y2 in d2.items():
                    if x2 in letters:
                        print(random.choice(y2))
            elif 'x' in letters:
                print(random.choice(random.choice(posList)))
            else:
                print('INVALID CHARACTER')
        print()

    elif sys.argv[1] == 'rand':  # Code block for "rand" subprogram
        while True:
            try:
                sys.argv[2] = int(sys.argv[2])
            except ValueError:
                print('Please enter the value as an integer.')
                f.close()
                exit()
            else:
                print()
                for number in range(sys.argv[2]):
                    print(random.choice(random.choice(posList)))
                print()
                f.close()
                exit()

    elif sys.argv[1] == 'thes':  # Code block for "thes" subprogram
        if len(sys.argv) == 4:
            if sys.argv[2] == 'x':
                for pos in posList:
                    for word in pos:
                        if word[0] == sys.argv[3]:
                            selectWords.append(word)
                print(random.choice(selectWords))
            elif sys.argv[2] in varLabels:
                if sys.argv[3] in alphas:
                    for x2, y2 in d2.items():
                        if sys.argv[2] == x2:
                            for word in y2:
                                if word[0] == '-' or word[0] == '+':
                                    if word[1] == sys.argv[3]:
                                        selectWords.append(word)
                                elif word[0] == sys.argv[3]:
                                    selectWords.append(word)
                    print()
                    print(random.choice(selectWords))
                    print()
                else:
                    print(str(sys.argv[3]) + ' not alpha. Run "python ap.py help".')
            else:
                print(str(sys.argv[2]) + ' not in list. Run "python ap.py help".')
        else:
            print('Incomplete input. Run "python ap.py help".')

    else:
        print('Incorrect input. Run "python ap.py help".')

else:
    print('Incorrect input. Run "python ap.py help".')

f.close()
exit()
