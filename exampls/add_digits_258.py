def add_digits(num):
    if num == 0:
        return 0
    return 1 + (num - 1) % 9


add_digits(234)