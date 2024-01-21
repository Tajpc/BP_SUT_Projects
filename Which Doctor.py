def get_binary_representation(value, width=32):
    binary_string = bin(value)[2:]
    return '0' * (width - len(binary_string)) + binary_string

def count_different_bits(a, b):
    bit_counter = 0
    for bit_a, bit_b in zip(a, b):
        if bit_a != bit_b:
            bit_counter += 1
    return bit_counter

def main():
    a = get_binary_representation(int(input()))
    b = get_binary_representation(int(input()))

    bit_counter = count_different_bits(a, b)

    print(bit_counter)

if __name__ == "__main__":
    main()
# Changes made:

# 1. Extracted the binary representation logic into a separate function `get_binary_representation` for reusability. Added a default width of 32 bits.
# 2. Moved the bit comparison logic into a separate function `count_different_bits` for better readability and reusability.
# 3. Used the `zip` function to iterate through corresponding bits in `a` and `b`.
# 4. Added a `main` function for better structure and reusability.