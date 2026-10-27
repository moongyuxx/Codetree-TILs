n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
a = n-3
arr = []

for i in range(a+1):
    for j in range(a+1):
        total = 0
        for k in range(i, i+3):
            total += sum(grid[k][j:j+3])
        arr.append(total)

print(max(arr))
