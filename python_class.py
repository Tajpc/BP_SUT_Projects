print("Hello\n Welcome to Geometric and Arithmetic sequence problems solver")
while True:
    name = input("Enter the type of sequence" + "(G or A): ")
    if name.islower():
        name = name.upper()
    if name == "A":
        ty = input("enter the type of question" + "((first/last number q= fl)\n(first/next number q= fn)): ")
        if ty == "fl":
            x = int(input("enter the first number: "))
            y = int(input("enter the last number: "))
            z = int(input("enter the number of (d): "))
            s = 0
            for i in range(x, y + 1, z):
                s += i
            print(s)
            break
        if ty == "fn":
            x = float(input("enter the first number: "))
            y = float(input("enter the next number: "))
            z = (y - x)
            num = int(input("Add how many variables you want: "))
            s = (num / 2) * ((x * 2) + (num - 1) * z)
            print("The sum of " + str(num) + " variables of this sequence\n is equal to : " + str(s))
            break
        elif ty != "fl" and ty != "fn":
            print("error")
    if name == "G":
        x = float(input("Enter the first number: "))
        y = float(input("Enter the next number: "))
        num = int(input("Add how many variables you want: "))
        res = y / x
        s = (x * (1-(pow(res, num))) / (1 - res))
        print("The sum of " + str(num) + " variables of this sequence\n is equal to : " + str(s))
        break
    elif name != "G" and name != "A":
        print("error")
