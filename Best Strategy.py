def isprime(n):
    if n <= 1:
        return False
    for item in range(2, int(n/2)+1):
            if (n % item) == 0:
                return False
    return True
def prime_counter(a, b):
    s = 0
    if a < b :
        for i in range(a, b+1):
            if isprime(i) == True:
                s += 1
    else:
        for i in range(b, a+1):
            if isprime(i) == True:
                s += 1
    return s


a , b = map(int, input(). split())
x = prime_counter(a, b)
if a <= b :
    print("main order - amount: ", x)
else:
    print("reverse order - amount: ", x)