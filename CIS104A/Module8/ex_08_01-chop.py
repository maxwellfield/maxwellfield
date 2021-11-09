def chop(list):
    del list[0]
    del list[-1]

numlist = [1, 2, 3, 4]

choplist = chop(numlist)
print(numlist)
print(choplist)
