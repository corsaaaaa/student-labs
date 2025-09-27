list = input().split()
d = {}
for i in set(list):
     d[i] = list.count(i)
mx = max(i for i in d.values())
print(*(k for k, v in d.items() if v == mx))