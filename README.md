# WordleSolver
A simple solver for wordle in python

Wordle: https://www.powerlanguage.co.uk/wordle/

Word source: https://github.com/dwyl/english-words

## Usage:

- Run the program with `python ./main.py`
- Enter your current gues sin the from `*a*b*`, where the letters are the confirmed letters/positions, and * are the unknown letters.
- Optionally add a # followed by excluded letters like: `*a*b*#cd`
- Optionally add a + after the excluded letters followed by included letters like: `*a*b*#cd+ef`
- The program will output possible solutions

## Future updates:

- Set up automatic character exclusion when known to not be in the word
- Set up better parsing when letters are known to be in the word, but not their position
