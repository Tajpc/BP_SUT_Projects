def get_binary_representation(value):
    binary_string = bin(value)[2:]
    return '0' * (32 - len(binary_string)) + binary_string

def main():
    first_32bit = get_binary_representation(int(input()))
    next_32bit = get_binary_representation(int(input()))
    guest_bit = (next_32bit + first_32bit)[::-1]

    guest_list = []
    n = int(input())
    index_list = [int(input()) for _ in range(n)]

    for index in index_list:
        guest_list.append('yes' if guest_bit[index] == '1' else 'no')

    for item in guest_list:
        print(item)

if __name__ == "__main__":
    main()

# Changes made:

# 1. Extracted the binary representation logic into a separate function `get_binary_representation` for reusability.
# 2. Used a single call to `get_binary_representation` for both `first_32bit` and `next_32bit`.
# 3. Combined the reversal of `guest_bit` and the loop for creating `guest_list` for better readability.
# 4. Added a `main` function for better structure and reusability.