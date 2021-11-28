text = 'mbox-short.txt'
alphabet = list ('abcdefghijklmnopqrstuvwxyz')
for letter in alphabet:
    print (letter + ': ' + str(text.count(letter)))
