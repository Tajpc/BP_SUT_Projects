first_32bit= bin(int(input()))[2:]
next_32bit = bin(int(input()))[2:]
if len(first_32bit) < 32:
    first_32bit = '0' * (32 - len(first_32bit)) + first_32bit
if len(next_32bit) < 32:
    next_32bit = '0' * (32 - len(next_32bit)) + next_32bit
guest_bit = next_32bit + first_32bit
guest_bit = guest_bit[::-1]
guest_list = []
n = int(input())
index_list = [int(input()) for i in range(n)]
for index in index_list :
    if guest_bit[index] == '1':
        guest_list.append('yes')
    else:
        guest_list.append('no')

for item in guest_list:
  print(item)