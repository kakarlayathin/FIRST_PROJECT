print("===buy_sell_stock===")
def max_price(prices):
    minimum_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        price = prices[i]
        profit = price - minimum_price
        if profit >max_profit:
            max_profit = profit

        if price<minimum_price:
                minimum_price = price
    return max_profit

print(max_price([7, 1, 5, 3, 6, 4]))  # Expected: 5
print(max_price([7, 6, 4, 3, 1]))     # Expected: 0
print(max_price([1, 2, 3, 4, 5]))     # Expected: 4 (buy at 1, sell at 5)