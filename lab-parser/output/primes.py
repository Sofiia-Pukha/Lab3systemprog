# Код згенеровано транслятором з підмножини мови C
import math

n = 0
k = 0
is_prime = 0
n = 2
while n <= 30:
    is_prime = 1
    k = 2
    while ((k * k) <= n) and bool(is_prime):
        if int(math.fmod(n, k)) == 0:
            is_prime = 0
        k = k + 1
    if is_prime:
        print('%d ' % (n,), end="")
    n = n + 1
print('\n', end="")
x = 15
if (x > 10) and (int(math.fmod(x, 2)) == 1):
    print('%d більше 10 і непарне\n' % (x,), end="")
elif x > 10:
    print('%d більше 10 і парне\n' % (x,), end="")
else:
    print('%d не більше 10\n' % (x,), end="")
