import random  # Enable random functions through relevant python library

f = open('2of12id.txt','rt')  # Open dictionary text file for reading

a = []  # Empty variable for adjectives
c = []  # Empty variable for conjunctions/prepositions
i = []  # Empty variable for interjections
n = []  # Empty variable for nouns
p = []  # Empty variable for pronouns
s = []  # Empty variable for spoken contractions
v = []  # Empty variable for verbs
x = []  # Empty variable for miscellaneous lines
vars = [a,c,i,n,p,s,v,x]  # List of all part-of-speech variables

for line in f:  # Loop through each line of the dict, adding lines to relevant variables according to their listed part of speech
    if 'A:' in line:
        a.append(line)
    elif 'C:' in line:
        c.append(line)
    elif 'I:' in line:
        i.append(line)
    elif 'N:' in line:
        n.append(line)
    elif 'P:' in line:
        p.append(line)
    elif 'S:' in line:
        s.append(line)
    elif 'V:' in line:
        v.append(line)
    else:
        x.append(line)  # Any lines that don't have a part of speech assigned

usrInput = input('Please choose between "preset" or "random" format: ')
if 'exit' in usrInput:
    f.close()
    exit()
else:
    while (usrInput != 'preset') and (usrInput != 'random'):
        if 'exit' in usrInput:
            f.close()
            exit()
        else:
            usrInput = input('Sorry, please try again: ')

if usrInput == 'preset':
    while True:
        usrInput = input('Please enter desired format: ')
        if 'exit' in usrInput:
            f.close()
            exit()
        else:
            for letters in usrInput:
                if 'a' in letters:
                    print(random.choice(a))
                elif 'c' in letters:
                    print(random.choice(c))
                elif 'i' in letters:
                    print(random.choice(i))
                elif 'n' in letters:
                    print(random.choice(n))
                elif 'p' in letters:
                    print(random.choice(p))
                elif 's' in letters:
                    print(random.choice(s))
                elif 'v' in letters:
                    print(random.choice(v))
                elif 'x' in letters:
                    print(random.choice(x))
                elif '_' in letters:
                    print(random.choice(random.choice(vars)))
                elif 'exit' in usrInput:
                    f.close()
                    exit()
                else:
                    print('INVALID CHARACTER')

elif usrInput == 'random':
    while True:
        try:
            usrInput = input('Please enter a numerical format length: ')
            if 'exit' in usrInput:
                f.close()
                exit()
            else:
                usrInput = int(usrInput)
        except ValueError:
                print('Please enter the value as an integer.')
                continue
        else:
            for number in range(usrInput):
                print(random.choice(random.choice(vars)))
