arr = [1,2,3,4,5]

print(list(enumerate(arr)))  # print [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]


fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

# 0 apple
# 1 banana
# 2 cherry
