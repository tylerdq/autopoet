import click, random, string

with open('words.txt', 'rt') as input_file:
    words = input_file.read().splitlines()
a, c, i, n, p, s, v = [], [], [], [], [], [], []  # Empty POS lists
posList = [a, c, i, n, p, s, v]  # Meta-list of all part-of-speech lists
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


@click.command()
@click.argument('format')
@click.option('--stanzas', '-s', default=1,
              help='Number of stanzas to generate.')
@click.option('--thes', '-t', is_flag=True,
              help='Starting letters for word(s).')
@click.option('--wait', '-w', is_flag=True,
              help='Whether to wait after each line.')
def form(format, stanzas, wait):
    """Utility to write poems with your computer."""
    poem = []
    for stanza in range(0, stanzas):
        for letters in format:
            if any(z in letters for z in d2.keys()):
                for x2, y2 in d2.items():
                    if x2 in letters:
                        poem.append(random.choice(y2))
            elif 'x' in letters:
                poem.append(random.choice(random.choice(posList)))
            else:
                poem.append('INVALID CHARACTER')
        poem.append('')
    if wait:
        click.echo()
        for line in poem:
            if line == '':
                print(line)
            else:
                usrInput = input(line + '\n')
            if usrInput == '*':
                print()
                exit()
    else:
        click.echo()
        for line in poem:
            click.echo(line)

if __name__ == '__main__':
    form()
