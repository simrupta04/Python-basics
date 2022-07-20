#9 Polar Cordinates
import cmath
complex_no = input("input the number ")
complex_no = complex(complex_no)
polar_coordinates = list(cmath.polar(complex_no))
for i in polar_coordinates:
    print(i)