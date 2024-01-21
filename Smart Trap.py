def tam(n):
   sum = 0
   for i in range(1, n+1):
    if n % i == 0:
       sum += i
   return sum


def numberToBase(sum, b):
    if sum == 0:
        return '0'
    digits = ''
    while sum:
        digits = digits + str(int(sum % b))
        sum //= b
    return digits[::-1]

blist = []
res = 0
while True:
    n, b = map(int, input().split())
    blist.append(b)
    res += int(numberToBase(tam(n), b))
    if n and b == -1:
        break
x = ''
for i in blist:
    if i not in range(2, 10) and i != -1:
        x = 'invalid base!'

if x != 'invalid base!':
    print(res)
else:
    print(x)