import sys
import random
inputfile = sys.argv[1]
outputfile = sys.argv[2]
maxword = int(sys.argv[3])
firstword = sys.argv[4]

with open(inputfile) as file_object:
  inputwords = file_object.read().split()

following_word = {}
for n in range(0, len(inputwords)-1):
    word = inputwords[n].strip().lower()
    if word not in following_word:
        next_word = inputwords[n+1].strip().lower()
        following_word[word] = [next_word]
    else:
        next_word = inputwords[n+1].strip().lower()
        l = following_word[word]
        l.append(next_word)

markov_chain = [firstword]
try:
    markov_chain.append(random.choice(following_word[firstword]))
except KeyError:
    print("Your first word must appear in the input file")
while maxword > 0:
    lastword = markov_chain[-1]
    if lastword not in following_word:
        print("cannot predict following word.")
        break
    following_selection = random.choice(following_word[lastword])
    markov_chain.append(following_selection)
    maxword = maxword - 1


with open(outputfile, 'w') as file_object:
        file_object.write(str(markov_chain))
 
