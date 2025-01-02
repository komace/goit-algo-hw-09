import timeit

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount -= coin * result[coin]

    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 1]
    min_coins = [float("inf")] * (amount + 1)
    coin_used = [0] * (amount + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

print(find_coins_greedy(99))
print(find_min_coins(99))

time_greedy = timeit.timeit('find_coins_greedy(99)', globals=globals(), number=10000)
print(f"Жадібний алгоритм виконався за: {time_greedy} секунд")

time_dynamic = timeit.timeit('find_min_coins(99)', globals=globals(), number=10000)
print(f"Динамічне програмування виконалось за: {time_dynamic} секунд")