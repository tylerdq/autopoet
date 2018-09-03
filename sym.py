import click, random, string

with open('dictionary.txt', 'rt') as input_file:
    words = input_file.read().splitlines()
a, c, i, n, p, s, v = [], [], [], [], [], [], []
posList = [a, c, i, n, p, s, v]  # Meta-list of all part-of-speech lists
textLabels = ['A:', 'C:', 'I:', 'N:', 'P:', 'S:', 'V:']
varLabels = ['a', 'c', 'i', 'n', 'p', 's', 'v']
alphas = list(string.ascii_lowercase)  # List of all lc alpha characters
d1 = dict(zip(textLabels, posList))
d2 = dict(zip(varLabels, posList))
for line in words:  # Add lines in dictionary file to pos lists
    for x1, y1 in d1.items():
        if x1 in line:
            y1.append(line.strip())


@click.group()
def cli():
    pass


@cli.command()
@click.argument('pattern')
@click.option('--output', '-o', default='output.txt',
              help='Specify output file name.')
@click.option('--stanzas', '-s', default=1,
              help='Number of stanzas to generate.')
@click.option('--wait', '-w', is_flag=True,
              help='Wait for input after each line.')
def poet(pattern, output, stanzas, wait):
    """Utility to cultivate poetic ideas.
    Generate word(s) arranged in PATTERN.\n
    PATTERN is a string including any combination of:\n
    adjective/adverb: a; conjunction/preposition: c; interjection: i; noun: n;
    pronoun: p; spoken contraction: s; verb: v; any previous: x\n
    Like this: python sym.py poet avnx -s 2 -w -o mypoem.txt"""
    inPoem, outPoem = [], []
    for stanza in range(0, stanzas):
        for letters in pattern:
            if any(z in letters for z in d2.keys()):
                for x2, y2 in d2.items():
                    if x2 in letters:
                        inPoem.append(random.choice(y2))
            elif 'x' in letters:
                inPoem.append(random.choice(random.choice(posList)))
            else:
                inPoem.append('INVALID PART OF SPEECH')
        inPoem.append('')
    if wait:
        click.echo()
        for item in inPoem:
            if item == '':
                click.echo(item)
                outPoem.append(item)
            else:
                usrInput = input(item + '\n')
                outPoem.append(item)
                outPoem.append(usrInput)
            if usrInput == '*':
                click.echo()
                exit()
    else:
        click.echo()
        for item in inPoem:
            click.echo(item)
            outPoem.append(item)
    if output:
        with open(output, 'w') as output_file:
            output_file.write('\n'.join(outPoem))


@cli.command()
@click.argument('partofspeech')
@click.argument('letters')
@click.option('--all', '-a', is_flag=True,
              help='Return all possible words.')
@click.option('--begin', '-b', is_flag=True,
              help='Specify if word(s) must begin with LETTERS')
@click.option('--output', '-o', default='output.txt',
              help='Specify output file name (only for --all).')
def find(partofspeech, letters, all, begin, output):
    """Utility to identify potential words.
    Generate word(s) from PARTOFSPEECH category with starting LETTERS.\n
    PARTOFSPEECH must include exactly one of:\n
    adjective/adverb: a; conjunction/preposition: c; interjection: i; noun: n;
    pronoun: p; spoken contraction: s; verb: v; any previous: x\n
    Like this: python sym.py find n intro -b -a -o mywords.txt"""
    selectWords = []
    click.echo()
    if partofspeech == 'x':
        for pos in posList:
            for word in pos:
                if begin:
                    if word.startswith(letters):
                        selectWords.append(word)
                else:
                    if letters in word:
                        selectWords.append(word)
    elif partofspeech in varLabels:
        if letters.isalpha():
            for x2, y2 in d2.items():
                if partofspeech == x2:
                    for word in y2:
                        if begin:
                            if word.startswith(letters):
                                selectWords.append(word)
                        else:
                            if letters in word:
                                selectWords.append(word)
    if len(selectWords) == 0:
        click.echo('No results. Try a less specific query.')
    elif all:
        trimmedWords = set(selectWords)
        finalWords = sorted(trimmedWords)
        for item in finalWords:
            click.echo(item)
        click.echo()
        if output:
            with open(output, 'w') as output_file:
                output_file.write('\n'.join(finalWords))
    else:
        finalWords = random.choice(selectWords)
        click.echo(finalWords)
        click.echo()


if __name__ == '__main__':
    cli()
