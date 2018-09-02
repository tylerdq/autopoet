# sympoiesis
sympoiesis is a set of utilities that supports inventive writing by facilitating contingent encounters with language.

## Installation
1. Install [Python 3](https://www.python.org/downloads/).
2. [Download](https://github.com/tylerdq/sympoiesis/archive/master.zip) or clone this repository
3. From the command line (Terminal, PowerShell, cmd, etc.) [`cd`](https://www.git-tower.com/learn/git/ebook/en/command-line/appendix/command-line-101) into the downloaded/cloned directory.
4. `pip3 install click`

## Usage
`python sym.py --help`  
`python sym.py poet --help`  
`python sym.py thes --help`

### Input Format
In case more explanation is needed beyond the in-script help, the commands require a code specifying the desired part(s) of speech. The script will print a number of appropriate words as requested. Part-of-speech codes can include:

* Adjectives/adverbs - `a`
* Conjunctions/prepositions - `c`
* Interjections - `i`
* Nouns - `n`
* Pronouns - `p`
* Spoken contractions - `s`
* Verbs - `v`
* Any of the above - `x`

A sample input format for "poet" might be `avnx`, which will output an adjective, verb, and noun plus one random part of speech. Input for "thes" must include any single character above.

*If characters other than the preset values above are passed to "poet", the script will return "INVALID CHARACTER" as an error code for that word, but still generate the other words.*

## Miscellaneous Notes
### Output Format
The script returns one or more lines from the [dictionary file](words.txt), most of which contain multiple versions of each word (suffixes, including tenses and pluralization). The choice to return full lines instead of parsing through the lines was made to encourage the user to select versions of words that might be most appropriate.

*Example (interpreted/refined) outputs from "poet" can be viewed in [outputs.md](outputs.md)*

### Notes on Dictionary File
The dictionary used is [2of12id](http://wordlist.aspell.net/alt12dicts-infl-readme/) from 12dicts and is called "dictionary.txt" in the working directory. If this file is moved or edited the script will break or not work as intended.

The [dictionary file](dictionary.txt) has been edited using the following processes:  
1. find: `([A-Z])\s([^:]*):` replace: `$2 $1:` (isolate POS codes to make subprograms work)
2. find: `^\+` replace: `` (remove `+` from line beginnings to make `thes` work)
3. find: `^-` replace: `` (remove `-` from line beginnings to make `thes` work)

### Notes on Name
This script used to be called *autopoet*. Inspiration for the name change to *sympoiesis* ("making with") courtesy of Donna Haraway and Abby Roche.