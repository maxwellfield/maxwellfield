name = input('Enter file name: ')
hand = open(name)
dotw = dict()
for line in hand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in dotw:
            dotw[words[2]] = 1
        else:
            dotw[words[2]] += 1
print(dotw)
