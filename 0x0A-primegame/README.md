# 🎮 **Prime Game**

This project involves solving an interview coding challenge that centers around a mathematical game involving prime numbers.

## 📝 **Tasks To Complete**

### ✅ **0. Prime Game**  
**File:** [0-prime_game.py](0-prime_game.py)

#### 📖 **Challenge Overview:**
Maria and Ben are playing a game with the following rules:

- They start with a set of consecutive integers from `1` to `n` (inclusive).
- Players take turns choosing a prime number from the set.
  - Once a prime number is chosen, that number and all of its multiples are removed from the set.
- The player who cannot make a move (because there are no more primes left to choose) loses the game.
- **Maria** always goes first, and both players play optimally.

#### 🎯 **Objective:**
Determine who wins the most rounds after playing `x` rounds, where `n` can differ for each round.

#### 🚦 **Requirements:**
- **Function Prototype:** `def isWinner(x, nums)`
- **Parameters:**
  - `x` (int): The number of rounds.
  - `nums` (list): A list of integers representing the upper limit `n` for each round.
- **Return:**
  - The name of the player that won the most rounds (`"Maria"` or `"Ben"`).
  - If the winner cannot be determined (tie or invalid input), return `None`.
- **Constraints:**
  - You can assume `n` and `x` will not exceed 10,000.
  - No external libraries or packages are allowed.

#### 🧩 **Example:**
- **Input:**  
  ```python
  x = 3
  nums = [4, 5, 1]
  ```
- **Game Analysis:**
  - **Round 1:** `n = 4`
    - Maria picks `2` → removes `2, 4` → Remaining: `1, 3`
    - Ben picks `3` → removes `3` → Remaining: `1`
    - **Ben** wins (no primes left for Maria).
  - **Round 2:** `n = 5`
    - Maria picks `2` → removes `2, 4` → Remaining: `1, 3, 5`
    - Ben picks `3` → removes `3` → Remaining: `1, 5`
    - Maria picks `5` → removes `5` → Remaining: `1`
    - **Maria** wins (no primes left for Ben).
  - **Round 3:** `n = 1`
    - **Ben** wins (no primes available for Maria to choose).
- **Result:**  
  **Ben** wins 2 rounds, **Maria** wins 1 round.  
  **Output:** `"Ben"`

#### 🛠 **Example Usage:**
```python
>>> print(isWinner(3, [4, 5, 1]))
"Ben"
```

### 📌 **Key Insights:**
- The game's complexity comes from efficiently determining the prime numbers within a given range, making the **Sieve of Eratosthenes** a critical component of the solution.
- This solution ensures both players make the most optimal moves, which involves picking primes that maximize their chances of winning.

