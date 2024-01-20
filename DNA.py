def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx = right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result

import re
class Plankton:
    dna_file = ''
    def __init__(self):
        pass

class Krab(Plankton):
    def dna(self, n):
        def file(n):
            self.dna_file += n + n[:10]
            return self.dna_file
        Krab.dna_file = re.sub('tt', 'o', file(n))
        return Krab.dna_file
        

class bob(Krab):
    def dna(self, n):
        l = []
        for i in str(len(super().dna(n))):
            l.append(i)
        return ''.join(merge_sort(l))    
class Squidward(Plankton):
    def search(arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i
    def dna(self, n):
        pattern = re.compile(r'(\w)\1\1')
        if re.search('x', n):
            self.dna_file +=  n + str(Squidward.search(n, 'x'))
            self.dna_file = pattern.sub('(0_0)', self.dna_file)
        else:
            self.dna_file = n
            self.dna_file = pattern.sub('(0_0)', self.dna_file)
        return self.dna_file

n = input()
krab = Krab()
squidward = Squidward()
sbob = bob()
def reverse_string(input_str):
    if len(input_str) > 0 and (input_str[0] not in {'m', 's'}) and (input_str[-1] in {'m', 's'}):
        reversed_str = input_str[::-1]
        return reversed_str
    else:
        return input_str

n = reverse_string(n)
if re.search('^m', n):
    print(krab.dna(n))
elif re.search('^sb', n):
    print(sbob.dna(n))
elif re.search('^s', n):
    print(squidward.dna(n))
else:
    print('invalid input')