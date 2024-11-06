def n_queens(n):
    def solve(r):
        if r == n:
            res.append(board[:])
        for c in range(n):
            if c in cols or r - c in diags1 or r + c in diags2: continue
            cols.add(c); diags1.add(r - c); diags2.add(r + c)
            board[r] = "." * c + "Q" + "." * (n - c - 1)
            solve(r + 1)
            cols.remove(c); diags1.remove(r - c); diags2.remove(r + c)

    res, board = [], ["." * n] * n
    cols, diags1, diags2 = set(), set(), set()
    solve(0)
    return res

# Example usage
n = int(input("Enter number of queens: "))
solutions = n_queens(n)
print(f"Total solutions: {len(solutions)}")
for solution in solutions:
    print("\n".join(solution), "\n")
