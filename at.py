import sys  # Enable passing command line arguments to script
import random  # Enable random functions from python library
import string  # Enable listing of ASCII characters

f = open('2of12id(rev).txt', 'rt')  # Open dictionary text file for reading

if sys.argv[1] == 'help':
    print('autothes usage:\n"python at.py <part of speech> <letter>"\nWhere <part of speech> is any of: a, c, i, n, p, s, or v\nAnd where <letter> is any lowercase character from a-z')
    f.close()
    exit()

elif len(sys.argv) == 3:

    a,c,i,n,p,s,v = [],[],[],[],[],[],[]  # Empty lists for parts of speech
    posList = [a,c,i,n,p,s,v]  # Meta-list of all part-of-speech lists
    textLabels = ['A:', 'C:', 'I:', 'N:', 'P:', 'S:', 'V:']
    varLabels = ['a', 'c', 'i', 'n', 'p', 's', 'v']
    alphas = list(string.ascii_lowercase)  # List of all lc alpha characters
    selectWords = []
    d1 = dict(zip(textLabels,posList))
    d2 = dict(zip(varLabels,posList))

    if sys.argv[1] in varLabels:  # Code block for handling arguments
        if sys.argv[2] in alphas:
            for x2, y2 in d2.items():
                if sys.argv[1] == x2:
                    for word in y2:
                        if word[0] == sys.argv[2]:
                                selectWords.append(word)
            print(random.choice(selectWords))
        else:
            print(str(sys.argv[2]) + ' not alpha. Run "python ay.py help" for help.')
    else:
        print(str(sys.argv[1]) + ' not in list. Run "python ay.py help" for help.')

else:
    print('Incomplete input. Run "python ay.py help" for help.')

f.close()
exit()
