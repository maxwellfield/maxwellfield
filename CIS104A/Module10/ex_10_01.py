name = input('Enter file name: ')
hand = open(name)
addresses = dict()
tup = list()
for line in hand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in addresses:
            addresses[words[1]] = 1
        else:
            addresses[words[1]] += 1
for key, val in list(addresses.items()):
    tup.append((val, key))
tup.sort(reverse=True)
for count, email in tup[:1]:
    print(email, count)
