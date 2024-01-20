from re import findall
n = int(input())
email_list = [input() for item in range(n)]
domain_list = []
for i in email_list:
    domain_list.append(str(findall("@[a-z]+.[a-z]+", i)))
for x in sorted(set(domain_list)):
    print(x[3:-2])