a = []
t = 1

for i in range(1, 5):
    b = []
    for j in range(t, t + 3):
        b.append(j)
    t +=3
    a.append(b)
print(a)