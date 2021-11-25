import math

a = input('a:')
b = input('b:')
c = input('c:')
i = 0
if a[0].isdigit() or a[0] == '-':
    if a[1:].isdigit() or len(a) == 1:
        a = float(a)
        i += 1
if b[0].isdigit() or b[0] == '-':
    if b[1:].isdigit() or len(b) == 1:
        b = float(b)
        i += 1
if c[0].isdigit() or c[0] == '-':
    if c[1:].isdigit() or len(c) == 1:
        c = float(c)
        i += 1
if i == 3:
    d = b * b - 4 * a * c
    if d > 0:
        x1 = (b - math.sqrt(d)) / (2 * a)
        x2 = (b + math.sqrt(d)) / (2 * a)
        print('roots: {} {}'.format(x1, x2))
    elif d == 0:
        x1 = (b - math.sqrt(d)) / (2 * a)
        print('root: {}'.format(x1))
    else:
        x1 = complex(b, math.sqrt(abs(d))) / (2 * a)
        x2 = complex(b, -math.sqrt(abs(d))) / (2 * a)
        print('roots: {} {}'.format(x1, x2))
