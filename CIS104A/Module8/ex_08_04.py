word_list = []
fh = open('romeo.txt')
for line in fh:
    words = line.split()
    for word in words:
        if word in word_list:
            continue
        word_list.append(word)
print(sorted(word_list))
