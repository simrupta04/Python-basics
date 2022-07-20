# 10 Find angle MBC
import math
side_ab = float(input("The length of side AB:"))
side_bc = float(input("The length of side BC:"))
deg_sign = u'\N{DEGREE SIGN}'
print(str(int(round(math.degrees(math.atan(side_ab/side_bc)),0))) + deg_sign)
