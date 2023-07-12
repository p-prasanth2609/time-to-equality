a = list(map(int, input().split()))
sum = 0
max = float('-inf')

for i in range(len(a)):
    if a[i] > max:
        max = a[i]
for i in range(len(a)):
    n=max-a[i]
    sum+=n
print(sum)
