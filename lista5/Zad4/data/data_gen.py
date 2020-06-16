import random
import sys



n = int(sys.argv[1])
p = []
for _ in range(n):
    p.append((random.uniform(-10, 10), random.uniform(-10, 10)))

print(n)
for i in range(n):
    for j in range(i+1, n):
        # a^2 + b^2 <= c^2
        weight = ((p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2)**0.5
        print(i, j, weight)
