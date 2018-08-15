# autopoet
autopoet is a little interactive script that draws on the alternative dictionary [2of12id](http://wordlist.aspell.net/alt12dicts-infl-readme/) from 12dicts to create poems of any length composed of whichever parts of speech the user prefers

## Usage
Install [Python 3](https://www.python.org/downloads/). Download or clone the repository, then open a terminal, `cd` into the directory, and run:

`python3 ap.py form <option>` or `python3 ap.py rand <option>`, where `<option>` is either an alphanumeric input format (if entered with "form") or an integer (if entered with "rand"). Run `python3 ap.py help` for basic instructions.

The basic difference between "form" and "rand" is that with "form", you tell the script which parts of speech you would like it to use in which order (see next section), while with "rand", you merely tell the script how many parts of speech to generate, and it assigns the requested number of random parts of speech.

*There is also a verbose (guided) version of the script you can use by running `python3 files/apv.py`. Check its [readme](files/READMEv.md) for more information.*

## Input Format
When the "form" option is chosen, the script needs to be given a format by feeding it arrangements of parts of speech. The output will print random words speech equal to the number of letters entered. Possible parts of speech include:

* Adjectives/adverbs - `a`
* Conjunctions/prepositions - `c`
* Interjections - `i`
* Nouns - `n`
* Pronouns - `p`
* Spoken contractions - `s`
* Verbs - `v`
* Any of the above - `x`

A sample input format might be `avnx`, which results in an output such as "adjective verb noun" plus one random part of speech.

*If values other than the above are entered, the script will return "INVALID CHARACTER" as an error code for the relevant line, but still generate the other lines.*

## Output Format
The script returns verbatim lines from the 2of12id dictionary, most of which contain multiple versions of each word (suffixes, including tenses and pluralization). The choice to return full lines instead of parsing through the lines was made to encourage the user to take additional creative steps post-script by choosing which versions of words work best for the usage at hand.

*Example script outputs can be viewed in [outputs.md](/outputs.md)*

## Notes on Dictionary File
The 2of12id dictionary was first edited using the following processes to make it simpler to parse in python:

1. find: `([A-Z])\s([^:]*):`
2. replace: `$2 $1:`

The original dictionary file is also saved in the repository as a reference backup.