matrix = [list(map(int, input().split())) for _ in range(int(input("Enter number of rows: ")))]
transpose = list(zip(*matrix))
print("Transpose:")
for row in transpose:
    print(*row)
