N = int(input())
arr = []

for i in range(N):
    line = input().split()
    if line[0] == "push_back":
        arr.append(line[1])
    elif line[0] == "pop_back":
        arr.pop()
    elif line[0] == "size":
        print(len(arr))
    else:
        print(arr[int(line[1]) - 1])