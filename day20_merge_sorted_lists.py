print("===merge_sorted_lists===")
def merge_lists(list1 , list2):
    result = []
    i = 0
    j = 0
    while i <len(list1) and j< len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i = i +1
        else:
            result.append(list2[j])
            j = j+1
    while i < len(list1):
        result.append(list1[i])
        i = i+1
    while j < len(list2):
        result.append(list2[j])
        j = j+1
    return result

print(merge_lists([1, 2, 4], [1, 3, 4]))  # Expected: [1, 1, 2, 3, 4, 4]
print(merge_lists([], [0]))               # Expected: [0]
print(merge_lists([1, 5], [2, 3, 6]))     # Expected: [1, 2, 3, 5, 6]
print(merge_lists([10, 20], [1, 2, 3]))