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
print(random.choice(v),'my\n',random.choice(n))
f.close()
