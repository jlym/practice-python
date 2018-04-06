import sys
inputfile = sys.argv[1]
outputfile = sys.argv[2]

with open(inputfile) as file_object:
  inputwords = file_object.read().split()

frequency = {}
for word in inputwords:
    word = word.strip().lower()
    if word in frequency:
        frequency[word] +=1
    else:
        frequency[word] = 1

frequent_word = sorted(frequency.items(), key=lambda x: x[1], reverse = True)
top_10 = str(frequent_word[0:9])

with open(outputfile, 'w') as file_object:
        file_object.write(top_10)
 