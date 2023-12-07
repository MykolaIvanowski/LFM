from typing import List


def isBadVersion(n):
    if n > 3:
        return True
    return False

def firstBadVersion( n: int) -> int:

    l = 0
    h = n

    while h >= l:
        m = (h + l) // 2
        b = isBadVersion(m)
        b1 = isBadVersion(m + 1)
        if not b and b1:
            return m + 1
        elif b:
            h = m - 1
        elif not b:
            l = m + 1
    return 1


# print(firstBadVersion(5))


def searchInsert( nums: List[int], target: int) -> int:

    low = 0
    high = len(nums) - 1
    middle = 0
    while high >= low:
        middle = (low+high)//2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            high = middle - 1

        elif nums[middle] < target:
            low = middle + 1

    if middle == 0 and nums[middle] > target:
        return 0
    elif nums[middle] > target:
        return middle
    elif nums[middle] < target:
        return middle + 1
arr = [1,3]
# print(searchInsert(arr, 2))

def moveZeroes( nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    index = 0
    stop = len(nums) - 1
    while stop != index:
        item = nums[index]
        if item == 0:
            nums.pop(index)
            nums.append(0)
            stop -= 1
            index -= 1
        index += 1
a = [1,2,3,4,7,0,0,3,4,3]
moveZeroes(a)
# print(a)



def x (s):
    s = s.split()
    x =[]
    for i in s:
        r = list(i)
        r.reverse()
        x.append(''.join(r))
    return ' '.join(x)

# print(x('asdf ghe 12345 rty jk'))

def x (s):
    s = s.split()
    x = []
    for i in s:
        r = list(i)
        left = 0
        right = len(r)-1
        while left <= right:
            r[left], r[right] = r[right], r[left]
            left += 1
            right -= 1
        x.append(''.join(r))
    return ' '.join(x)

# print(x('asdf ghe 12345 rty jk'))


def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    base_color = image[sr][sc]
    image[sr][sc] = color
    if base_color == color:
        return image
    # down
    if len(image) - 1 >= sr + 1 and image[sr + 1][sc] == base_color:
        floodFill(image, sr+1, sc, color)
        image[sr + 1][sc] = color

    # up
    if sr - 1 >= 0 and image[sr - 1][sc] == base_color:
        floodFill(image, sr-1, sc, color)
        image[sr - 1][sc] = color

    # right
    if len(image[sr]) - 1 >= sc + 1 and image[sr][sc + 1] == base_color:
        floodFill(image, sr, sc+1, color)
        image[sr][sc + 1] = color

    # left
    if sc - 1 >= 0 and image[sr][sc - 1] == base_color:
        floodFill(image, sr, sc-1, color)
        image[sr][sc - 1] = color
    return image

print(floodFill([[1,1,1,1],[1,1,0,1],[1,0,1,1]],1,1,2))


li = [0]

def p(li):
    li[0]=1

    
    li =[0,2]
    li.append(5)

p(li)
print(li)

listA = [0]
listB = listA
listB.append(1)
p(listB)
print(listA)