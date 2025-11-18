n = int(input())
boots = []
pares = 0
for i in range(n):
    current_boot = list(map(str, input().split()))
    found = False
    for j in boots:
        if current_boot[0] == j[0] and current_boot[1] != j[1]:
            pares += 1
            boots.remove(j)
            found = True
            break
    if not found:
        boots.append(current_boot)
print(pares)