/* Прості числа до 30
   та перевірка числа через if / else if / else */
int n;
int k;
int is_prime;

for (n = 2; n <= 30; n++) {
    is_prime = 1;
    k = 2;
    while (k * k <= n && is_prime) {
        if (n % k == 0)
            is_prime = 0;
        k++;
    }
    if (is_prime)
        printf("%d ", n);
}
printf("\n");

int x = 15;
if (x > 10 && x % 2 == 1)
    printf("%d більше 10 і непарне\n", x);
else if (x > 10)
    printf("%d більше 10 і парне\n", x);
else
    printf("%d не більше 10\n", x);
