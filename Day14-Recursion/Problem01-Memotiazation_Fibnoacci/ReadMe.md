# Fibonacci Series using Memoization (Python)

## Description

This script calculates the Fibonacci sequence using recursion combined with Python’s built-in `lru_cache` for memoization. Memoization helps optimize the recursive approach by storing previously computed results, significantly improving performance for repeated function calls.

## How It Works

- The `fibonacci(n)` function is decorated with `@lru_cache(maxsize=1000)` to cache results of previous calls.
- For each number `n`, it computes the nth Fibonacci number recursively.
- The results are printed in the format: `n : fibonacci(n)`

## Example Output

1 : 1
2 : 1
3 : 2
4 : 3
5 : 5
...


## Important Notes

- Python has a default recursion depth limit (~1000). Calling the function with `n` values larger than that will cause a `RecursionError`.
- The current code runs:
  ```python
  for n in range(1, 20000):
This will exceed the recursion limit. To avoid errors, reduce the range to something like:


for n in range(1, 1000):
