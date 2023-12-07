def plus_one(digits):

    for k, v in reversed(list(enumerate(digits))):
        if v < 9:
            digits[k] += 1
            return digits
        digits[k] = 0
    return [1] + digits


print(plus_one([1,2,3,4,5,7,98]))