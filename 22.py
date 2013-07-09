import string

f = open("names.txt","r")

names = f.read()
names = string.lower(names)
names = names.translate(None, '"')
names = names.split((','))
names.sort()


alphabet = string.ascii_lowercase
scoreSum = 0
for i in xrange(len(names)):
    score=0
    for letter in names[i]:
        score += alphabet.index(letter)+1
    score *= i+1
    scoreSum += score

print scoreSum
