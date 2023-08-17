data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25,27]
target = 0


def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False


print(binary_search_iterative(data, target))


def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid - 1)
        else:
            return binary_search_recursive(data, target, mid + 1, high)


print(binary_search_recursive(data, target, 0, len(data) - 1))
