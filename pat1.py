import re
char = input()
char_list = char.split(' ')
char_list2 = []
num_list = []
for i in char_list:
    if i.isdigit() and len(i) == 2:
        char_list2.append(str(re.findall("^[0-9]", i))[2])
        num_list.append(int(str(re.findall("[0-9]$", i))[2:-2]))
    else:
        char_list2.append(str(re.findall("^.|^[0-9]", i))[2])
        num_list.append(int(str(re.findall("[0-9]$|[0-9]{2}$", i))[2:-2]))
res = {}
for key in num_list:
    for value in char_list2:
        res[key] = value
        char_list2.remove(value)
        break
result_list = sorted(res.items())
for result in result_list:
    print(result[1], end='')