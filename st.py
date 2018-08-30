with open('poem.txt', 'rt') as poem:
    for line in poem:
        line.strip()
        usrInput = input(line)
        if usrInput == '*':
            exit()
