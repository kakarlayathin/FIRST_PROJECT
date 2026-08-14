print("===climbing_stairs===")
def climb_stairs(n):
    if n<=2:
        return n
    prev2 = 1
    prev1 = 2
    for i in range(3, n+1):
        current = prev1 +prev2
        prev2 = prev1
        prev1 = current
    return prev1
print(climb_stairs(2))  # Expected: 2
print(climb_stairs(3))  # Expected: 3
print(climb_stairs(4))  # Expected: 5
print(climb_stairs(5))  # Expected: 8