# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fhand = open(fname)
count = 0
tot = 0
ans = 0
for line in fhand:
	if not line.startswith("X-DSPAM-Confidence:") : continue
	count = count + 1
	num = float(line[21:])
	tot = num + tot
ans = tot / count
print("Average spam confidence:", ans)
