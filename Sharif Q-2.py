a = bin(int(input()))[2:]
b = bin(int(input()))[2:]
bit_counter = 0
if len(a) > len(b):
    b = ('0'* (len(a) - len(b))) + b
else:
    a = ('0'* (len(b) - len(a))) + a
for i in range (max(len(a), len(b))):
    if a[i] != b[i]:
        bit_counter += 1

print(bit_counter)