#water jug problem
def rule_applied(before, after):
    x1, y1 = before
    x2, y2 = after

    if x2 > x1 and y2 == y1:
        return "Fill Jug1"
    elif y2 > y1 and x2 == x1:
        return "Fill Jug2"
    elif x2 < x1 and y2 == y1:
        return "Empty Jug1"
    elif y2 < y1 and x2 == x1:
        return "Empty Jug2"
    elif x2 < x1 and y2 > y1:
        return "Pour Jug1 → Jug2"
    elif x2 > x1 and y2 < y1:
        return "Pour Jug2 → Jug1"
    else:
        return "No action"


def water_jug_dfs(jug1, jug2, target):
    stack = [(0, 0, [])]  
    visited = set()

    while stack:
        x, y, path = stack.pop()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        path = path + [(x, y)]

        if x == target or y == target:
            print("\nSolution Found:\n")
            for i in range(len(path) - 1):
                action = rule_applied(path[i], path[i + 1])
                print(f"Step {i + 1}: {action} → {path[i + 1]}")
            return

        next_states = [
            (jug1, y),                # Fill Jug1
            (x, jug2),                # Fill Jug2
            (0, y),                   # Empty Jug1
            (x, 0),                   # Empty Jug2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),  # Pour Jug1 → Jug2
            (x + min(y, jug1 - x), y - min(y, jug1 - x))   # Pour Jug2 → Jug1
        ]

        for state in next_states:
            if state not in visited:
                stack.append((state[0], state[1], path))

   
jug1 = int(input("Enter Jug1 capacity: "))
jug2 = int(input("Enter Jug2 capacity: "))
target = int(input("Target amount of water: "))

water_jug_dfs(jug1, jug2, target)
