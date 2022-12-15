def chocolateFeast(n, c, m):
    total_money = n
    products = int(n / c)
    if products >= m:
        change = int(products)
        while change > 0:
            change = change - m
            if change >= 0:
                products += 1
                change += 1
    return products