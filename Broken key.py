def plus(a, b):
  while b != 0:
    c = a & b 
    a = a ^ b 
    b = c << 1 
  return a

a = int(input())
b = int(input())
k = int(input())
print(plus(a, b))
if k == plus(a, b):
  print("YES")
else:
    print("NO")