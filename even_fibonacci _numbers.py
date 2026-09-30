
"""Even Fibonacci Sum Calculator.

Calculates the sum of all even Fibonacci numbers that do not exceed N.
Utilizes the recurrence relation: E(k) = 4 * E(k-1) + E(k-2)
where E(k) represents the k-th even Fibonacci number.
"""

def sum_even_fibonacci_sequence(limit : int) -> int:
    """
        in fibonacci even num ocuure every 3 value  => it is f3n , f3n+3 , ....
        f3n = 4 * f3n-3 + f3n-6
    """

    if limit <= 2:
        return 0
    
    prev_even = 2
    curr_even = 8
    total_sum = prev_even                        
    while curr_even < limit:
        total_sum += curr_even
        prev_even, curr_even = curr_even, 4 * curr_even + prev_even
    return total_sum

def main():
    "Handles I/O "
    test_cases = int(input().strip())
    if not test_cases:
        return 0

    for a in range(test_cases) :
        limit = int(input().strip())
        print(sum_even_fibonacci_sequence(limit))

if __name__ == "__main__":
    main()









