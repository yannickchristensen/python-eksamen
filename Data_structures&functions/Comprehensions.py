# List comprehension
# [expression for value in collection]

evenOne = []
for i in range(50):
    if i%2==0:
        evenOne.append(i)


evenTwo = [i for i in range(50) if i%2==0]

print(evenOne)
print(evenTwo)

