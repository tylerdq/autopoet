import random  # Enable random functions through relevant python library

f = open('2of12id.txt','rt')  # Open dictionary text file for reading

a,c,i,n,p,s,v,m = [],[],[],[],[],[],[],[]  # Empty lists for parts of speech
d1 = {'A:':a, 'C:':c, 'I:':i, 'N:':n, 'P:':p, 'S:':s, 'V:':v}
posList = [a,c,i,n,p,s,v]  # List of all part-of-speech variables

for line in f:  # Loop dictionary file lines, adding lines to pos variables
    for x, y in d1.items():
        if x in line:
            y.append(line)
        else:
            m.append(line)  # Lines that don't have a part of speech assigned

# Initial input prompt
usrInput = input('Please choose between "preset", "random", or "thes": ')
if 'exit' in usrInput:
    f.close()
    exit()
else:
    while (usrInput != 'preset') and (usrInput != 'random') and (usrInput != 'thes'):
        if 'exit' in usrInput:
            f.close()
            exit()
        else:
            usrInput = input('Sorry, please try again: ')

# Actions to take if "preset" is entered in initial input
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
                elif 'm' in letters:
                    print(random.choice(m))
                elif '_' in letters:
                    print(random.choice(random.choice(posList)))
                elif 'exit' in usrInput:
                    f.close()
                    exit()
                else:
                    print('INVALID CHARACTER')

# Actions to take if "random" is entered in initial input
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
                print(random.choice(random.choice(posList)))

# Actions to take if "thes" is entered in intial input.
elif usrInput == 'thes':
    usrInput1 = input('Please enter a part of speech code: ')
    if 'exit' in usrInput1:
        f.close()
        exit()
    else:
        while (usrInput1 != ('a' or 'c' or 'i' or 'n' or 'p' or 's' or 'v' or 'x')):
            if 'exit' in usrInput1:
                f.close()
                exit()
            else:
                usrInput = input('Sorry, please try again: ')
