import click, random, string

with open('dictionary.txt', 'rt') as input_file:
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


@click.group()
def cli():
    pass


@cli.command()
@click.argument('pattern')
@click.option('--stanzas', '-s', default=1,
              help='Number of stanzas to generate.')
#@click.option('--thes', '-t', is_flag=True,
#              help='Starting letters for word(s).')
@click.option('--wait', '-w', is_flag=True,
              help='Wait for input after each line.')
def poet(pattern, stanzas, wait):
    """Utility to cultivate poetic ideas.
    Generate word(s) arranged in PATTERN.\n
    PATTERN is a string including any combination of:\n
    adjective/adverb: a; conjunction/preposition: c; interjection: i; noun: n;
    pronoun: p; spoken contraction: s; verb: v; any previous: x\n
    Like this: python sym.py poet avnx -s 2 -w"""
    poem = []
    for stanza in range(0, stanzas):
        for letters in pattern:
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
                click.echo()
                exit()
    else:
        click.echo()
        for line in poem:
            click.echo(line)


@cli.command()
@click.argument('partofspeech')
@click.argument('letters')
@click.option('--count', '-c', default=1,
              help='Number of words to generate.')
def thes(partofspeech, letters, count):
    """Utility to identify potential words.
    Generate word(s) from PARTOFSPEECH category with starting LETTERS.\n
    PARTOFSPEECH must include exactly one of:\n
    adjective/adverb: a; conjunction/preposition: c; interjection: i; noun: n;
    pronoun: p; spoken contraction: s; verb: v; any previous: x\n
    Like this: python sym.py thes n und -c 7"""
    click.echo()
    if partofspeech == 'x':
        for pos in posList:
            for word in pos:
                if word.startswith(letters):
                    selectWords.append(word)
        if len(selectWords) == 0:
            click.echo('No results. Use a different combination.')
        else:
            for r in range(0, count):
                print(random.choice(selectWords))
    elif partofspeech in varLabels:
        if letters.isalpha():
            for x2, y2 in d2.items():
                if partofspeech == x2:
                    for word in y2:
                        if word.startswith(letters):
                            selectWords.append(word)
            if len(selectWords) == 0:
                click.echo('No results. Use a different combination.')
            else:
                for r in range(0, count):
                    click.echo(random.choice(selectWords))
    click.echo()


if __name__ == '__main__':
    cli()
