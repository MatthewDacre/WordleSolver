import random

global allWords
def print_help():
    print("* Enter a 5 letter pattern. The patter takes the form of:\n*")
    print("* \tLower case letter for a position where you know the letter")
    print("* \t* for a position where the letter is unknown\n*")
    print("* Enter -rand x for x random full words\n\n")

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
print("Enter -help for usage")
guess = input("Enter current pattern: \n")

while guess != "-1":
    parse(guess)
    guess = input("Enter current pattern: \n")