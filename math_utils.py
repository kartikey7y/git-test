"""Math utility functions."""

import math
from typing import List


def factorial(n: int) -> int:
    """Return factorial of n."""
    if n < 0:
        raise ValueError("n must be non-negative")
    return math.prod(range(1, n + 1), start=1)


def is_prime(n: int) -> bool:
    """Check if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> List[int]:
    """Generate first n Fibonacci numbers."""
    if n <= 0:
        return []
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]


def gcd(a: int, b: int) -> int:
    """Return greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return abs(a)


if __name__ == "__main__":
    print(f"factorial(5) = {factorial(5)}")
    print(f"is_prime(17) = {is_prime(17)}")
    print(f"fibonacci(10) = {fibonacci(10)}")
    print(f"gcd(48, 18) = {gcd(48, 18)}")
