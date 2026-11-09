// Факторіал (while) і сума чисел (for)
int n = 6;
int f = 1;
int i = 1;

while (i <= n) {
    f = f * i;
    i++;
}
printf("%d! = %d\n", n, f);

int sum = 0;
for (i = 1; i <= 10; i++) {
    sum = sum + i;
}
printf("Сума 1..10 = %d\n", sum);
