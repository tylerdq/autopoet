# autopoet
autopoet is a little program that  create poems of any length composed of whichever parts of speech the user prefers. It also can act as a "thesaurus" to help identify unanticipated single words based on a chosen part of speech and starting letter.

## Usage
Install [Python 3](https://www.python.org/downloads/). Download or clone the repository, then open a terminal, `cd` into the directory, and run:

`python ap.py <subprogram> <option1> <option2> <option3>`

### Subprograms
* "help" will print help text.
* "form" is the main subprogram, and requires an input format (see below) in `<option1>` to produce a poem with that format. A positive integer can be entered in `<option2>` can be used to specify how many stanzas of this format to generate.
* "rand" produces fully random poems (both part of speech categories and their words are randomized), and requires a positive integer in `<option1>` to specify how many words are produced. A positive integer can also be entered in `<option2>` to specify how many stanzas to generate.
* "thes" is an extra program that requires an single format code (see below) in `<option1>` as well as any set of starting letters from a-z in `<option2>`. It will produce a word from the desired part of speech with starting letters equal to `<option2>`. A positive integer can be entered in `<option3>` to specify how many matching words to generate.

### Input Format
When the "form" or "thes" subprograms are run, the program needs a coded format to return words that match the desired parts of speech. The output will print random words speech equal to the number of letters entered. Possible parts of speech include:

* Adjectives/adverbs - `a`
* Conjunctions/prepositions - `c`
* Interjections - `i`
* Nouns - `n`
* Pronouns - `p`
* Spoken contractions - `s`
* Verbs - `v`
* Any of the above - `x`

A sample input format for the "form" subprogram might be `avnx`, which results in an output such as "adjective verb noun" plus one random part of speech. For the "thes" subprogram it could be any option, which will be further constrained by the starting letter(s) in arg2.

*If characters other than the preset values above are entered during the "form" subprogram, the script will return "INVALID CHARACTER" as an error code for the relevant line, but still generate the other lines.*

## Output Format
The script returns one or more verbatim lines from the 2of12id dictionary, most of which contain multiple versions of each word (suffixes, including tenses and pluralization). The choice to return full lines instead of parsing through the lines was made to encourage the user to take additional creative steps post-script by choosing which versions of words work best for the usage at hand.

*Example (interpreted/refined) outputs from the "form" and "rand" subprograms can be viewed in [outputs.md](outputs.md)*

## Notes on Dictionary File
The dictionary used is [2of12id](http://wordlist.aspell.net/alt12dicts-infl-readme/) from 12dicts. The [dictionary file](words.txt) has been edited using the following processes to make it simpler to parse:

1. find: `([A-Z])\s([^:]*):` replace: `$2 $1:` (isolate POS codes to make subprograms work)
2. find: `^\+` replace: `` (remove `+` from line beginnings to make "thes" work)
3. find: `^-` replace: `` (remove `-` from line beginnings to make "thes" work)