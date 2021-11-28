text = 'mbox-short.txt'
alpha = list ('abcdefghijklmnopqrstuvwxyz')
for letter in alpha:
    print (letter + ': ' + str(text.count(letter)))
