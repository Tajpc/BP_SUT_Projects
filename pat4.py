def find_pairs(nums, target_sum):
    num_indices = {}
    found = False
    res = []
    for i, num in enumerate(nums):
        complement = target_sum - num
        if complement in num_indices:
            found = True
            res.append(num_indices[complement] + i)
        num_indices[num] = i
    if not found:
        print("Not Found!")
    else:
        for f in sorted(res):
            print(f)
nums = [int(i) for i in input().split()]
target_sum = int(input())
find_pairs(nums, target_sum)