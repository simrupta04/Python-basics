#23 Mapped and Lambda Function
l=[]
def fibonacci(n):
        a=0
        b=1
        # l=[]
        if n==0:
             pass
        elif n==1:
             l.append(a)
        else:
            l.append(a)
            l.append(b)
            for i in range (2,n):
                c=a+b
                a=b
                b=c
                l.append(c)
        return l
n=int(input("enter a number"))
print("fibonacci series are:" ,fibonacci(n))
cube_fab = list(map(lambda x: x**3, l))
print("cube of fibonacci series are:" ,cube_fab)