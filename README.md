# sympoiesis

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tylerdq/sympoiesis/jupyter?filepath=sym.ipynb)

sympoiesis is a set of utilities that supports inventive writing by facilitating contingent encounters with language.

## Installation
1. Install [Python 3](https://www.python.org/downloads/).
2. [Download](https://github.com/tylerdq/sympoiesis/archive/master.zip) or clone this repository.
3. From the command line ([Terminal](https://blog.galvanize.com/how-to-use-the-terminal-command-line/), [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/getting-started/getting-started-with-windows-powershell?view=powershell-6), cmd.exe, etc.) [`cd`](https://www.git-tower.com/learn/git/ebook/en/command-line/appendix/command-line-101) into the downloaded/cloned directory.
4. `pip3 install click`

## Usage
`python sym.py --help`  
`python sym.py poet --help`  
`python sym.py find --help`

### Parts of Speech
The commands require a code specifying the desired part(s) of speech. The program will generate a number of appropriate words as requested. Part-of-speech codes can include:

* Adjectives/adverbs - `a`
* Conjunctions/prepositions - `c`
* Nouns - `n`
* Pronouns - `p`
* Verbs - `v`
* Any of the above - `x`

Input for "poet" might include a string such as `avnx`, which will output an adjective, verb, and noun plus one random part of speech. Input for "find" must include a single character pertaining to any category above.

*If characters other than the preset values above are passed to "poet", the program will return "INVALID PART OF SPEECH" as an error code for that word, but still generate the other words.*

## Miscellaneous Notes
### Output Format
The program prints to the console and also saves to "output.txt" (unless an alternate filename is given). Output includes one or more lines from the [dictionary file](words.txt), most of which contain multiple versions of each word (tenses/pluralization).

*Example (interpreted/refined) outputs from "poet" can be viewed in [outputs.md](outputs.md)*

### Notes on Dictionary File
The dictionary used is [2of12id](http://wordlist.aspell.net/alt12dicts-infl-readme/) from 12dicts which appears in the working directory as "dictionary.txt". If this file is moved, renamed, or edited the program will probably break or not work as intended.

The [dictionary file](dictionary.txt) has been pre-processed by taking the following steps in a text editor:  
1. find: `([A-Z])\s([^:]*):` replace: `$2 $1:` (isolate POS codes to make subprograms work)
2. find: `^\+` replace: `` (remove `+` from line beginnings to make `find` work)
3. find: `^-` replace: `` (remove `-` from line beginnings to make `find` work)

### Notes on Name
This program used to be called *autopoet*. Inspiration for the name change to *sympoiesis* ("making with") courtesy of [Donna Haraway](https://slowrotation.memoryoftheworld.org/Donna%20J.%20Haraway/Staying%20With%20the%20Trouble_%20Making%20K%20(31237)/Staying%20With%20the%20Trouble_%20Makin%20-%20Donna%20J.%20Haraway.pdf#page=22) and Abby Roche.