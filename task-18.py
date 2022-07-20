#18 Incorrect regex
import re;
n = int(input("Enter the number:"))
for _ in range(n):
    try:
        re.compile(input("Enter the expression:"))
        Output = True
    except re.error:
        Output = False
    print(Output)