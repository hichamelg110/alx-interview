#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """
    . Generate primes up to n using Sieve of Eratosthenes .
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for v in range(i*i, n + 1, i):
                sieve[v] = False
    
    return sieve

def isWinner(x, nums):
    """
    . Determine Prime Game winner for x rounds with given n values .
    """
    if not nums or x < 1:
        return None
    
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    def game_winner(n):
        """
        . Determine winner for a single game with n .
        """
        count = sum(1 for i in range(2, n + 1) if primes[i])
        return "Maria" if count % 2 == 1 else "Ben"
    
    maria_wins = sum(1 for n in nums if game_winner(n) == "Maria")
    ben_wins = x - maria_wins
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
