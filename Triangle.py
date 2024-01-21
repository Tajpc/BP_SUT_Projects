def printpascal(n):
    arr = [1]
    temp = []
    for i in range(n):
        for j in range(len(arr)):
            print(arr[j], end= " ")
        print()
        temp.append(1)
        for j in range(len(arr)-1):
            temp.append(arr[j] + arr[j+1])
        temp.append(1)
        arr = temp
        temp = []

n = int(input())
printpascal(n)

# nothing to change:))