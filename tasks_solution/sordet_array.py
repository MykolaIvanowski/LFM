# leetcode task
# given two sorted arrays size m and n respectively. return median fo two sorted arrays
# the overall run complexity should be O( log(m+n) )

num1 = [1, 2, 3, 4, 5]
num2 = [4, 5, 8, 9, 10]


num = num1 + num2
print(num)
if len(num) % 2 == 0:
    x = int(len(num)/2)
    print((num[x] + num[x-1])/2)
else:
    print(num[int(len(num) / 2)])
