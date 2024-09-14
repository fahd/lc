def maxProfit(self, prices: List[int]) -> int:
    local_min = prices[0]
    gp = 0

    for i in range(1,len(prices)):
        price = prices[i]
        diff = price - local_min
        if price < local_min:
            local_min = price
            continue
        if diff > gp:
            gp = diff
    return gp

