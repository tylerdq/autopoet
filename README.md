# autopoet
autopoet is a little interactive script that draws on the alternative dictionary [2of12id](http://wordlist.aspell.net/alt12dicts-infl-readme/) from 12dicts to create poems of any length composed of whichever parts of speech the user prefers

# Usage
Install [Python 3](https://www.python.org/downloads/). Download or clone the repository, then open a terminal, `cd` into the directory, and run:

`python3 ap.py`

Upon execution, the script will invite the user to choose between using a "preset" format or a "random" one. Enter `preset` to specify which parts of speech the program should generate. Enter `random` to specify a poem length and let the script randomly assign a number of parts of speech equal to the specified length. Input and output formats are explained in more detail in the next two sections.

At any point, the user can type "exit" to leave the program.

## Input Format
When the "preset" option is chosen, the script needs to be given a format by feeding it arrangements of parts of speech. The output will print a random part of speech in the order requested. Possible parts of speech include:
* Adjectives - `a`
* Conjunctions/prepositions - `c`
* Interjections - `i`
* Nouns - `n`
* Pronouns - `p`
* Spoken contractions - `s`
* Verbs - `v`
* Miscellaneous items - `x`
* Any of the above - `_`

A sample input format might be `avn_`, which results in an output such as "adjective verb noun" plus one random part of speech.

*If values other than the above are entered, the script will return "INVALID CHARACTER" as an error code for the relevant line, but still generate the other lines.*

## Output Format
The script returns verbatim lines from the 2of12id dictionary, most of which contain multiple versions of the word (suffixes, including tenses and pluralization). The choice to return full lines instead of parsing through the lines was made to encourage the user to take additional creative steps post-script by choosing which versions of words work best for the usage at hand.

*Example script outputs can be viewed in [outputs.md](/outputs.md)*