array = [50, 25, 10, 5, 2, 1]


def exchange(coin):
    result = {}
    for i in array:
        if coin // i > 0:
            result[i] = coin // i
            coin = coin % i
    return result

print(exchange())