import math

min_value, max_value = map(int, input().split())

eratos = [True] * (max_value - min_value + 1)
for i in range(2, int(math.sqrt(max_value)) + 1):
    n = i ** 2
    if n > max_value:
        break

    a = math.ceil(min_value / n) * n
    while a <= max_value:
        eratos[a - min_value] = False
        a += n

print(eratos.count(True))
