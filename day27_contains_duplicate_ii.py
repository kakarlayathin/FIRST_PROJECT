print("===contains_duplicate_ii===")
def contains_nearby_duplicate(numbers, k):
    seen = {}
    for i in range(len(numbers)):
        num = numbers[i]
        if num in seen:
            distance = i - seen[num]
            if distance <= k:
                return True

        seen[num] = i
    return False

print(contains_nearby_duplicate([1, 2, 3, 1], 3))      # True
print(contains_nearby_duplicate([1, 0, 1, 1], 1))      # True
print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2)) # False