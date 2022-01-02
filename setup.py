fileAll = open(r"words.txt", "r")
fileFive = open(r"words_5letter.txt", "w")

lines = fileAll.readlines()

for word in lines:
    if len(word) == 6:
        fileFive.write(word)

fileAll.close()
fileFive.close()