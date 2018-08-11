#import click
import random

#with open('2of12id.txt') as f:
#    for line in f:
#        if 'A:' in line:  # Limit to adjective lines
#            randAdj =
#            print(line)
#        else:
#            randLine =

# Limit to adjectives only
#line = random.choice(open('2of12id.txt').readlines())

#if 'A:' in line:
#    print(line)
#else:

f = open('2of12id.txt','rt')
#words = f.read()
a = []  # Create empty variable for adjectives
c = []  # Create empty variable for conjunctions/prepositions
i = []  # Create empty variable for interjections
n = []  # Create empty variable for nouns
p = []  # Create empty variable for pronouns
s = []  # Create empty variable for spoken contractions
v = []  # Create empty variable for verbs
x = []  # Create empty variable for miscellaneous lines
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
print(random.choice(v),'my',random.choice(n))
f.close()
