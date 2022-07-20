#20 Zipped
X = int( input("enter the number "))
marks = []
for _ in range(X):
    marks.append(list(map(float, input("enter the marks").strip().split())))
for i in zip(*marks):
    print(sum(i)/len(i))