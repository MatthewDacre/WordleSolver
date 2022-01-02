global allWords

def parse(guess):
    if(len(guess) != 5):
        print("Length of guess incorrect:\nExpected 5, found {}".format(len(guess)))
    for i, c in enumerate(guess):
        if not c.isalpha() and not c == '*':
            print("Unexpected character at position {}: {}".format(i+1, c))
    
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
guess = input("Enter current pattern: \n")

while guess != "-1":
    parse(guess)
    guess = input("Enter current pattern: \n")