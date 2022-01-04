import random

global allWords
def print_help():
    print("\n\n")
    print("* Enter a 5 letter pattern. The patter takes the form of:")
    print("*\tLower case letter for a position where you know the letter")
    print("*\t* for a position where the letter is unknown")
    print("*\t* for a position where the letter is unknown")
    print("*\t* There are additional modifiers to filter:")
    print("*\t\t* add a # at the end of the pattern followed by all letter not included")
    print("* Enter -rand x for x random full words")
    print("* Enter -help for this help text\n")
    print("* Enter -1 to exit this program\n\n")

def print_rand(c):
    if(c != ' '):
        for _ in range(int(c)):
            print(random.choice(allWords))


def parse(guess):
    if(guess == "-help"):
        print_help()
        return
    if(guess[:5] == "-rand"):
        print_rand(guess[-1])
        return
    excluded = ""
    if("#" in guess):
        split = guess.split('#')
        guess = split[0]
        excluded = split[1]
    if(len(guess) != 5):
        print("Length of guess incorrect:\nExpected 5, found {}".format(len(guess)))
        return
    for i, c in enumerate(guess):
        if not c.isalpha() and not c == '*':
            print("Unexpected character at position {}: {}".format(i+1, c))
            return
    chars = [char for char in guess]
    print("\nPossible words:")
    for word in allWords:
        valid = True
        for c in list(excluded):
            if c in word:
                valid = False
        if valid:
            for pos, c in enumerate(word):
                if chars[pos] != '*':
                    if c != chars[pos]:
                        valid = False
        if valid:
            print(word)


file = open(r"words_5letter.txt", "r")
allWords_temp = file.readlines()
allWords = [x[:-1] for x in allWords_temp]
file.close()
print_help()
guess = input("Enter current pattern: \n")

while guess != "-1":
    parse(guess)
    guess = input("Enter current pattern: \n")