# autopoet
autopoet is a little program that draws on the alternative dictionary [2of12id](http://wordlist.aspell.net/alt12dicts-infl-readme/) from 12dicts to create poems of any length composed of whichever parts of speech the user prefers. It also can act as a "thesaurus" that can help identify new words based on the user's choice of part of speech and starting letter.

## Usage
Install [Python 3](https://www.python.org/downloads/). Download or clone the repository, then open a terminal, `cd` into the directory, and run:

`python3 ap.py <subprogram> <arg1> <arg2>` according to the following:
	* Subprograms include "form", "rand", and "thes"
	* If "form" subprogram was chosen, arg1 takes an input format (see next section) of arbitrary length and parts of speech and returns a randomized poem to match. If "rand" was chosen, arg1 takes any positive integer and returns a poem of matching length with parts of speech categories randomized as well. If "thes" was chosen, arg1 takes a single-character input format (see next section) and returns a part of speech from that category.
	* Arg2 is only required/available for the "thes" subprogram, and specifies the starting letter of the returned part of speech.

## Input Format
When the "form" or "thes" subprograms are run, the program needs a coded format to return words that match the desired parts of speech. The output will print random words speech equal to the number of letters entered. Possible parts of speech include:

* Adjectives/adverbs - `a`
* Conjunctions/prepositions - `c`
* Interjections - `i`
* Nouns - `n`
* Pronouns - `p`
* Spoken contractions - `s`
* Verbs - `v`
* Any of the above - `x`

A sample input format for the "form" subprogram might be `avnx`, which results in an output such as "adjective verb noun" plus one random part of speech. For the "thes" subprogram it could be any option, which will be further constrained by the starting letter in arg2.

*If characters other than the preset values above are entered during the "form" subprogram, the script will return "INVALID CHARACTER" as an error code for the relevant line, but still generate the other lines.*

## Output Format
The script returns one or more verbatim lines from the 2of12id dictionary, most of which contain multiple versions of each word (suffixes, including tenses and pluralization). The choice to return full lines instead of parsing through the lines was made to encourage the user to take additional creative steps post-script by choosing which versions of words work best for the usage at hand.

*Example outputs from the "form" and "rand" subprograms can be viewed in [outputs.md](outputs.md)*

## Notes on Dictionary File
The 2of12id dictionary was first edited using the following processes to make it simpler to parse in python:

1. find: `([A-Z])\s([^:]*):`
2. replace: `$2 $1:`