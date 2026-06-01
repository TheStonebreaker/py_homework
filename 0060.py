n = int(input())
lines = []
line = ""
for i in range(1, n + 1):
    line += str(i)
    lines.append(line)
    print(line)
for i in range(n - 2, -1, -1):
    print(lines[i])
