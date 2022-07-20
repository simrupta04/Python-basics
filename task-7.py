# n,m = map(int, input("Enter the contains integers n and m separated by a space:") .split())
elements = list(map(int, input("Enter the array element:").split()))
a = set(map(int, input("Enter the Element:").split()))
b = set(map(int, input("Enter the Element:").split()))
initial_happiness = 0
for i in elements:
    if i in a:
        initial_happiness += 1
    elif i in b:
        initial_happiness -= 1
    else:
        pass
print(initial_happiness)