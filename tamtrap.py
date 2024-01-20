def sum(arg):
  result = 0
  for i in arg:
    result += i
  return result
def average(arg):
  result = 0
  for i in arg:
    result += i
  return round(result / len(arg), 2)
def gcdplus(a, b):
    while (b):
       a, b = b, a % b
    return a
def gcd(arg):
  result = arg[0]
  for x in arg[1:]:
    if result < x:
      temp = result
      result = x
      x = temp
    while x != 0:
      temp = x
      x = result % x
      result = temp
  return result
def min(arg):
  result = arg[0]
  for i in arg:
    if i < result:
      result = i
  return result
def max(arg):
  result = arg[0]
  for i in arg:
    if i > result:
      result = i
  return result
arglist = []
funclist = ['sum', 'average', 'lcd','gcd', 'max', 'min']
func = input()
while True:
  if func not in funclist:
    print('Invalid command')
    break
  else:
    n = input()
    if n == 'end':
      break
    arglist.append(int(n))
if func == 'sum':
  print(sum(arglist))
elif func == 'average':
  print(average(arglist))
elif func == 'gcd':
  print(gcd(arglist))
elif func == 'lcd':
  lcd = 1
  for i in arglist:
    lcd = (lcd*i)//(gcdplus(lcd, i))
  print(lcd)
elif func == 'max':
  print(max(arglist))
elif func == 'min':
  print(min(arglist))
