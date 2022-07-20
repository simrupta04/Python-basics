#21 Athlete Sort
import math
import os
import random
import re
import sys
N, M = map(int, input("Enter the colounm and  rows").split())
rows = [input("enter the rank, age, height") for _ in range(N)]
K = int(input("enter the key"))
for row in sorted(rows, key=lambda row: int(row.split()[K])):
    print("Sorted rows:",row)