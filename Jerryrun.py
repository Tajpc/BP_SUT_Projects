col = int(input())
roadmap = ['.'] * col
result_list = []
roadmap[0] = '*'
i = 0
road = ''
while True:
    plan = input()
    if plan == 'END':
        break
    else:
        if plan == 'R':
            if i < col-1:
                i += 1
                roadmap[i] = '*'
        elif plan == 'L':
            if i != 0:
                i -= 1
                roadmap[i] = '*'
        elif plan == 'B':
            result_list.append(roadmap)
            roadmap = ['.'] * col
            roadmap[i] = '*'
result_list.append(roadmap)
for x in result_list:
    print(' '.join(x))
if result_list[-1][-1] == '.' or i != col-1:
    print("There's no way out!")