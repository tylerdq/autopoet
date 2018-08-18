# autopoet
autopoet is a little program that creates poems of any length composed of whichever parts of speech the user prefers. It also can act as a "thesaurus" to help identify unanticipated words based on a chosen part of speech and starting letter(s).

## Usage
Install [Python 3](https://www.python.org/downloads/). Then [download](https://github.com/tylerdq/autopoet/archive/master.zip) or clone this repository and from the command line (Terminal, PowerShell, cmd, etc.) [`cd`](https://www.git-tower.com/learn/git/ebook/en/command-line/appendix/command-line-101) into the downloaded/cloned directory and run:

`python ap.py <subprogram> <option1> <option2> <option3>`

### Subprograms
* `help` will print help text.
* `form` is the main subprogram, and requires an input format (see below) in `<option1>` to produce a poem with that format. A positive integer can be entered in `<option2>` to specify how many stanzas of this format to generate.
* `rand` produces fully random poems (both part of speech categories and their words are randomized), and requires a positive integer in `<option1>` to specify how many words are produced. A positive integer can also be entered in `<option2>` to specify how many stanzas to generate.
* `thes` is an extra program that requires an single format code (see below) in `<option1>` as well as any set of one or more starting letters from a-z in `<option2>`. It will produce a word from the desired part of speech with starting letters equal to `<option2>`. A positive integer can be entered in `<option3>` to specify how many matching words to generate.

### Input Format
When the `form` or `thes` subprograms are run, the program needs a code to find words that match the desired parts of speech. The output will print a number of appropriate words matching the code. Possible parts of speech include:

* Adjectives/adverbs - `a`
* Conjunctions/prepositions - `c`
* Interjections - `i`
* Nouns - `n`
* Pronouns - `p`
* Spoken contractions - `s`
* Verbs - `v`
* Any of the above - `x`

A sample input format for the `form` subprogram might be `avnx`, which outputs "adjective verb noun" plus one random part of speech. For the `thes` subprogram the format is any single character above.

*If characters other than the preset values above are entered during the `form` subprogram, the script will return "INVALID CHARACTER" as an error code for the relevant line, but still generate the other lines.*

## Output Format
The script returns one or lines from the [dictionary file](words.txt), most of which contain multiple versions of each word (suffixes, including tenses and pluralization). The choice to return full lines instead of parsing through the lines was made to encourage the user to select versions of words that might be most appropriate.

*Example (interpreted/refined) outputs from the `form` and `rand` subprograms can be viewed in [outputs.md](outputs.md)*

## Notes on Dictionary File
The dictionary used is [2of12id](http://wordlist.aspell.net/alt12dicts-infl-readme/) from 12dicts. The [dictionary file](words.txt) has been edited using the following processes:

1. find: `([A-Z])\s([^:]*):` replace: `$2 $1:` (isolate POS codes to make subprograms work)
2. find: `^\+` replace: `` (remove `+` from line beginnings to make `thes` work)
3. find: `^-` replace: `` (remove `-` from line beginnings to make `thes` work)