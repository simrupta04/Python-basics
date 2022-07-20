#11 Iter tools Product
import itertools
A = list(map(int, input("Enter the first list:").split()))
B = list(map(int, input("Enter the Second list").split()))
product_is = list(itertools.product(A, B))
for i in product_is:
    print(i, end=" ")