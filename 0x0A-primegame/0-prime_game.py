#!/usr/bin/python3
"""Module for Prime Game"""

def isWinner(rounds, nums):
    """
    Determines who wins the most rounds.

    Args:
        rounds (int): Number of rounds.
        nums (list): List where each integer represents the size of the set.

    Returns:
        str: "Ben" or "Maria" if one wins the most rounds, or None if tied.
    """
    if rounds <= 0 or nums is None or rounds != len(nums):
        return None

    ben_wins, maria_wins = 0, 0
    primes = [1] * (max(nums) + 1)
    primes[0], primes[1] = 0, 0

    for i in range(2, len(primes)):
        mark_multiples(primes, i)

    for num in nums:
        if sum(primes[:num + 1]) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins > maria_wins:
        return "Ben"
    if maria_wins > ben_wins:
        return "Maria"
    return None

def mark_multiples(prime_list, prime):
    """
    Marks multiples of a prime as non-prime.

    Args:
        prime_list (list): List of potential primes.
        prime (int): The prime number.
    """
    for i in range(2, len(prime_list)):
        try:
            prime_list[i * prime] = 0
        except IndexError:
            break
