def max_profit(prices):
    min_valUe = prices[0]
    max_sell = 0
    for i in prices:
        if i < min_valUe:
            min_valUe = i
        max_sell = max(max_sell, i - min_valUe)
    return max_sell


list_1 = [1,5,7,9,3,4,6]
list_2 = [7,6,3,2,1]
list_3 = [6,2,1,5,7,4,6]
list_4 = [2,4,1]

print(max_profit(list_1))
print(max_profit(list_2))
print(max_profit(list_3))
print(max_profit(list_4))
