# 25 Detect floating point Number
import re
class Main():
    def __init__(self):
        self.n = int(input("enter the number"))

        for i in range(self.n):
            self.s = input("enter the digit which u want to check")
            print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', self.s)))


if __name__ == '__main__':
    obj = Main()