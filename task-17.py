#17Exception
try:
    a=int(input("Enter the Value:"))
    b=int(input("Enter the Value:"))
    print(a/b)
except ZeroDivisionError as e:
        print("Error Code:",e);
except ValueError as v:
        print("Error Code:",v);