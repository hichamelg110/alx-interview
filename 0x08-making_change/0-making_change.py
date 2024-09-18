#!/usr/bin/python3
"""making change"""

def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet a given amount total
    
    Args:
        coins (list): List of coin denominations available
        total (int): Target amount
    
    Returns:
        int: Minimum number of coins needed, or -1 if not possible
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    coin_count = 0
    current_sum = 0

    for coin in coins:
        while current_sum + coin <= total:
            current_sum += coin
            coin_count += 1
        
        if current_sum == total:
            return coin_count

    return -1
