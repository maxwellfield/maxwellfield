name = input("Enter file:")
hand = open(name)
count = dict()
for line in hand:
    if line.startswith('From '):
        line=line.split()
        count[line[1]]=count.get(line[1],0)+1
bigword = None
bigcount = 0
for add,num in count.items():
  if bigcount ==0 or num>bigcount :
        bigcount=num
        bigword=add
print(bigword,bigcount)
