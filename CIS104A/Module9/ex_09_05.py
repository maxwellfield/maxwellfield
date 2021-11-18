name = input('Enter file name: ')
hand = open(name)
domcount = dict()
for line in hand:
	if line.startswith('From '):
		line = line.split()
		address = line[1]
		address = address.split('@')
		domain = address[1]
		domcount[domain] = domcount.get(domain,0) + 1
print(domcount)
