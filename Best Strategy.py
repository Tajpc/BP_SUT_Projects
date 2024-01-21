def is_prime(n):
    if n <= 1:
        return False
    for item in range(2, int(n/2) + 1):
        if n % item == 0:
            return False
    return True

def prime_counter(start, end):
    return sum(1 for i in range(start, end + 1) if is_prime(i))

def main():
    a, b = map(int, input().split())
    result = prime_counter(min(a, b), max(a, b))

    order = "main" if a <= b else "reverse"
    print(f"{order} order - amount: {result}")

if __name__ == "__main__":
    main()

# Changes made:

# 1. Renamed `isprime` to `is_prime` to follow the snake_case naming convention.
# 2. Used a generator expression inside `prime_counter` to count prime numbers efficiently.
# 3. Combined the logic for determining the order into the `main` function for better readability.
# 4. Added a `main` function and a check for `__name__` to allow for better modularization and reusability.
# 5. Used f-strings for formatting the output string.