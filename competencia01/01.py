n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    if i+1 not in a:
        print(i + 1)
        break