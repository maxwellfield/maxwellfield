han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    # Guardian Pattern
    if len(wds) < 3 :
        continue
    # Dangerous (Below)
    if wds[0] != 'From' :
        continue
    print(wds[2])
