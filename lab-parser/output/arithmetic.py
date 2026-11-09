# Код згенеровано транслятором з підмножини мови C
import math

a = 7
b = 3
x = 2.5
s = a + (b * 2)
d = int(a / b)
m = int(math.fmod(a, b))
r = ((a + b) * x) / 4
print('s = %d\n' % (s,), end="")
print('a / b = %d, a %% b = %d\n' % (d, m), end="")
print('r = %.2f\n' % (r,), end="")
print('-a + 10 = %d\n' % ((-a) + 10,), end="")
