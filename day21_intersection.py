print("===intersection===")
def intersection(list1,list2):
    result = []
    seen = {}
    for num in list1:
        seen[num] = True
    for num in list2:
        if num in seen:
            result.append(num)
            del seen[num]
    return result

print(intersection([1, 2, 2, 1], [2, 2]))                    # Expected: [2]
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))              # Expected: [9, 4] (or [4, 9])
print(intersection([1, 2, 3], [4, 5, 6]))                    # Expected: []