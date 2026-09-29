
"""Project Euler Problem 1: Multiples of 3 or 5.

Find the sum of all the multiples of 3 or 5 below N.
Uses Gauss's summation formula for an O(1) time complexity per query.
"""

import sys


def sum_multiples_of_k(k: int, limit: int) -> int:
    
    """Calculates the sum of all positive multiples of `k` strictly below `limit`.

    Uses the arithmetic series formula:
        k + 2k + ...+pk = k(1+2+..+p)   
        1 + 2 + ... + p = p * (p + 1) / 2     and   k + 2k + ...+pk  = k *  p * (p + 1) / 2 
        where p = (limit - 1) // k.  => pk = limit -1
    :param k: The factor/multiplier.
    :param limit: The upper bound (exclusive).
    :return: The sum of multiples of `k` less than `limit`.
    """
    if k <= 0 or limit <= 0:
        return 0
    
    p = (limit - 1) // k
    return k * p * (p + 1) // 2
   
def sum_multiples_of_3_and_5(limit: int) -> int:  
    """Calculates the sum of all multiples of 3 or 5 strictly below `limit`.

    Applies the Inclusion-Exclusion Principle:
        Sum = Sum(Multiples of 3) + Sum(Multiples of 5) - Sum(Multiples of 15)

    :param limit: The upper bound (exclusive).
    :return: The total sum of multiples of 3 or 5 below `limit`.
    """
    sum_3 = sum_multiples_of_k(3, limit)
    sum_5 = sum_multiples_of_k(5, limit)
    sum_15 = sum_multiples_of_k(15, limit)

    return sum_3 + sum_5 - sum_15


def main() -> None:
    """Handles standard I/O """
    test_cases = int(input().strip())
    if not test_cases:
        return

    for a in range(test_cases):
        n = int(input().strip())
        print(sum_multiples_of_3_and_5(n))

if __name__ == "__main__":
    main()