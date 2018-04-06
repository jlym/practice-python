import sys
inputfile = sys.argv[1]
outputfile = sys.argv[2]
maxword = sys.argv[3]
firstword = sys.argv[4]

with open(inputfile) as file_object:
  inputwords = file_object.read().split()

following_word = {}
for n in range(0, len(inputwords)-1):
    word = inputwords[n].strip().lower()
    if word not in following_word:
        next_word = inputwords[n+1]
        following_word[word] = [next_word]
    else:
        next_word = inputwords[n+1]
        l = following_word[word]
        l.append(next_word)
print(following_word)

