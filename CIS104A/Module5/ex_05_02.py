largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        val = float(num)
    except:
        print('Invalid input')
        continue

    if largest is None or val > largest:
        largest = val
    if smallest is None or val < smallest:
        smallest = val

print("Maximum is", int(largest))
print("Minimum is", int(smallest))
