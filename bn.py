import random

f = open('2of12id.txt','rt')

a = []  # Empty variable for adjectives
c = []  # Empty variable for conjunctions/prepositions
i = []  # Empty variable for interjections
n = []  # Empty variable for nouns
p = []  # Empty variable for pronouns
s = []  # Empty variable for spoken contractions
v = []  # Empty variable for verbs
x = []  # Empty variable for miscellaneous lines
vars = [a,c,i,n,p,s,v,x]

for line in f:
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
        x.append(line)

usr_input = input('Choose "preset" or "random" format: ')
while (usr_input != 'preset') and (usr_input != 'random'):
    usr_input = input('Sorry, please try again: ')

if usr_input == 'preset':
    usr_input = input('Enter format: ')
    if usr_input == 'avn':
            print(random.choice(a),random.choice(v),random.choice(n))
    elif usr_input == 'vn':
            print(random.choice(v),random.choice(n))

elif usr_input == 'random':
    print(random.choice(random.choice(vars)),random.choice(random.choice(vars)),random.choice(random.choice(vars)))

f.close()
