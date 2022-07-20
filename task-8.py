# 8.Symmetric Difference
M = int(input("enter a number"))
m = set(map(int, input("enter the element").split()))
N = int(input("enter the number"))
n = set(map(int, input("enter the element").split()))
m_difference = m.difference(n)
n_difference = n.difference(m)
difference = list(m_difference) + list(n_difference)
difference.sort()
for i in difference:
    print(i)