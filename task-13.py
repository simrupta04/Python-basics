#13 Default dict
from collections import defaultdict
x, y = map(int,input("Enter the size:").split())
a = defaultdict(list)
for i in range(1, x + 1):
    a[input("Enter the element:")].append(i)
for i in range(1, y + 1):
    k = input("Enter the second element:")
    if len(a[k]) > 0:
        print(" ".join(str(c) for c in a[k]))
    else:
        print(-1)