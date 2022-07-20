#19 Classes dealing with complex number
import sys
def output(num):
    real = num.real
    imag = num.imag

    if real == 0 and imag == 0:
        print('0.00')
    elif real == 0:
        print('{:.2f}i'.format(imag))
    elif imag == 0:
        print('{:.2f}'.format(real))
    else:
        print('{:.2f} {} {:.2f}i'.format(real, '-' if imag < 0 else '+', abs(imag)))
real1, imag1 = [float(x) for x in input("enter first real and imaginary number").split()]
real2, imag2 = [float(x) for x in input("enter second realand imaginary number").split()]
C1 = complex(real1, imag1)
C2 = complex(real2, imag2)
output(C1 + C2)
output(C1 - C2)
output(C1 * C2)
output(C1 / C2)
print('{:.2f}'.format(abs(C1)))
print('{:.2f}'.format(abs(C2)))