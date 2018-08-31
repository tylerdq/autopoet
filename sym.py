import sys, random, string

with open('words.txt', 'rt') as input_file:
    words = input_file.read().splitlines()

if len(sys.argv) == 1:
    print('Incomplete input. Run "python sym.py help".')
    exit()

elif len(sys.argv) == 2:
    if sys.argv[1] == 'help':
        print('\n"python sym.py <subprogram> <option1> <option2> <option3>"\n\n    Subprogram: "help", form", "rand", or "thes"\n    option1:\n        - "form": Any arbitrary combination of [a,c,i,n,p,s,v,x]\n        - "rand": Any positive integer\n        - "thes": Any one of [a,c,i,n,p,s,v]\n    option2:\n        - "form": Any positive integer (number of stanzas)\n        - "rand": Any positive integer (number of stanzas)\n        - "thes": Start of word (lowercase letters from a-z)\n    option3:\n        - "thes": Any positive integer (number of words)\n')
        exit()
    else:
        print('Incomplete input. Run "python sym.py help".')
        exit()

elif len(sys.argv) >= 3:
    a,c,i,n,p,s,v = [],[],[],[],[],[],[]  # Empty lists for parts of speech
    posList = [a,c,i,n,p,s,v]  # Meta-list of all part-of-speech lists
    textLabels = ['A:', 'C:', 'I:', 'N:', 'P:', 'S:', 'V:']
    varLabels = ['a', 'c', 'i', 'n', 'p', 's', 'v']
    alphas = list(string.ascii_lowercase)  # List of all lc alpha characters
    selectWords = []  # Empty list for "thes" subprogram
    d1 = dict(zip(textLabels, posList))
    d2 = dict(zip(varLabels, posList))

    for line in words:  # Loop through dictionary file, adding lines to pos lists
        for x1, y1 in d1.items():
            if x1 in line:
                y1.append(line.strip())

    if sys.argv[1] == 'form':  # Code block for "form" subprogram
        if len(sys.argv) >= 4:
            try:
                stanzas = int(sys.argv[3])
            except ValueError:
                stanzas = 1
        else:
            stanzas = 1
        poem = []
        for stanza in range(0, stanzas):
            for letters in sys.argv[2]:
                if any(z in letters for z in d2.keys()):
                    for x2, y2 in d2.items():
                        if x2 in letters:
                            poem.append(random.choice(y2))
                elif 'x' in letters:
                    poem.append(random.choice(random.choice(posList)))
                else:
                    poem.append('INVALID CHARACTER')
            poem.append('')
        if len(sys.argv) >= 4:
            if 'step' in sys.argv:
                for line in poem:
                    if line == '':
                        print(line)
                    else:
                        usrInput = input(line + '\n')
                    if usrInput == '*':
                        print()
                        exit()
            else:
                print()
                for line in poem:
                    print(line)
        else:
            print()
            for line in poem:
                print(line)

    elif sys.argv[1] == 'rand':  # Code block for "rand" subprogram

        while True:
            try:
                sys.argv[2] = int(sys.argv[2])
            except ValueError:
                print('Value must be entered as an integer.')
                exit()
            else:
                print()
                if len(sys.argv) == 4:
                    stanzas = int(sys.argv[3])
                else:
                    stanzas = 1
                for r in range(0,stanzas):
                    for number in range(sys.argv[2]):
                        print(random.choice(random.choice(posList)))
                    print()
                exit()

    elif sys.argv[1] == 'thes':  # Code block for "thes" subprogram
        print()
        if len(sys.argv) >= 4:
            if len(sys.argv) == 5:
                sax = int(sys.argv[4])
            else:
                sax = 1
            if sys.argv[2] == 'x':
                for pos in posList:
                    for word in pos:
                        if word.startswith(sys.argv[3]):
                            selectWords.append(word)
                if len(selectWords) == 0:
                    print('No results. Use a different combination.\n')
                else:
                    for r in range(0,sax):
                        print(random.choice(selectWords) + '\n')
            elif sys.argv[2] in varLabels:
                if sys.argv[3].isalpha():
                    for x2, y2 in d2.items():
                        if sys.argv[2] == x2:
                            for word in y2:
                                if word.startswith(sys.argv[3]):
                                    selectWords.append(word)
                    if len(selectWords) == 0:
                        print('No results. Use a different combination.\n')
                    else:
                        for r in range(0,sax):
                            print(random.choice(selectWords) + '\n')
                else:
                    print(str(sys.argv[3]) + ' is not alpha. Run "python sym.py help".')
            else:
                print(str(sys.argv[2]) + ' is not a valid POS code. Run "python sym.py help".\n')
        else:
            print('Incomplete input. Run "python sym.py help".\n')

    else:
        print('Incorrect input. Run "python sym.py help".')

else:
    print('Incorrect input. Run "python sym.py help".')

exit()
