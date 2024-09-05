#!/usr/bin/python3
"""
Prime game module.
"""

def isWinner(x, nums):
    """
    Determines the winner of a prime game session with `x` rounds.

    Parameters:
    - x: Number of rounds to be played.
    - nums: List of integers where each integer represents the upper limit of the range [1, n] for each round.

    Returns:
    - The name of the player who won the most rounds, either 'Maria' or 'Ben'. 
      If there is a tie or invalid input, returns None.
    """
    if x < 1 or not nums:
        return None

    maria_wins, ben_wins = 0, 0

    # Sieve of Eratosthenes to find all prime numbers up to the maximum number in nums
    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes

    for i in range(2, max_num + 1):
        if primes[i]:
            for multiple in range(i * 2, max_num + 1, i):
                primes[multiple] = False

    # Play each round to determine the winner
    for n in nums[:x]:
        prime_count = sum(primes[1:n + 1])  # Count primes up to n

        # Maria wins if there's  an odd number of primes, otherwise Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Return the overall winner, or None if it's a tie
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
if __name__ == "__main__":
    x = 3
    nums = [4, 5, 1]
    print(isWinner(x, nums))  # Expected output: "Ben"

