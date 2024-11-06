from collections import deque

c1, c2, t = map(int, input("Enter Jug1, Jug2 capacities and target: ").split())
q, v = deque([(0, 0, [])]), set()
while q:
    j1, j2, path = q.popleft()
    if (j1, j2) in v:
        continue
    v.add((j1, j2))
    path = path + [(j1, j2)]
    if j1 == t or j2 == t:
        print("Achievable")
        for state in path:
            print(state)
        break
    # Possible moves
    moves = [
        (c1, j2),  # Fill Jug1
        (j1, c2),  # Fill Jug2
        (0, j2),    # Empty Jug1
        (j1, 0),    # Empty Jug2
        (j1 - min(j1, c2 - j2), j2 + min(j1, c2 - j2)),  # Pour Jug1 -> Jug2
        (j1 + min(j2, c1 - j1), j2 - min(j2, c1 - j1))   # Pour Jug2 -> Jug1
    ]
    for state in moves:
        if state not in v:
            q.append((*state, path))
else:
    print("Not achievable")
