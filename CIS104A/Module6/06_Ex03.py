# word = 'banana'
# count = 0
# for letter in word:
    # if letter == 'a':
        # count = count + 1
# print(count)

def count(string, letter):
    count = 0
    for character in string:
        if character == letter:
            count = count + 1
    print(count)

count('banana', 'a')
