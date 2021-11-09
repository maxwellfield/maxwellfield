def middle(list):
    new = list[1:]
    del new[-1]
    return new

numlist = [1, 2, 3, 4]

midlist = middle(numlist)
print(numlist)
print(midlist)
