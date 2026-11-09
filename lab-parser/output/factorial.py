# Код згенеровано транслятором з підмножини мови C
import math

n = 6
f = 1
i = 1
while i <= n:
    f = f * i
    i = i + 1
print('%d! = %d\n' % (n, f), end="")
sum = 0
i = 1
while i <= 10:
    sum = sum + i
    i = i + 1
print('Сума 1..10 = %d\n' % (sum,), end="")
