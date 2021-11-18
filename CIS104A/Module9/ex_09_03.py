name = input('Enter file name: ')
hand = open(name)
count = dict()
for line in hand:
    if line.startswith('From:'):
        line = line.split()
        address = line[1]
        count[address] = count.get(address,0)+1
print(count)
