def print_board(b):
    print("\n".join(" | ".join(b[i * 3:(i + 1) * 3]) for i in range(3)), "\n" + "-" * 9)

def winner(b, p):
    return any(all(c == p for c in b[i * 3:(i + 1) * 3]) for i in range(3)) or \
           any(all(b[i + j * 3] == p for j in range(3)) for i in range(3)) or \
           all(b[i] == p for i in [0, 4, 8]) or \
           all(b[i] == p for i in [2, 4, 6])

b, p = [" "] * 9, "X"
for _ in range(9):
    print_board(b)
    while True:
        try:
            pos = int(input(f"Player {p}, choose a position (0-8): "))
            if b[pos] == " ":
                b[pos] = p
                break
            print("Taken! Try again.")
        except (ValueError, IndexError):
            print("Invalid input! Enter a number between 0 and 8.")
    if winner(b, p):
        print_board(b)
        print(f"Player {p} wins!")
        break
    p = "O" if p == "X" else "X"
else:
    print_board(b)
    print("It's a tie!")
