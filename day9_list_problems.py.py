print("===PROBLEM 1: Find the Maximum Number===")
def find_max(numbers):
    max_val =numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

print(find_max([3, 1, 9, 4, 2]))
print(find_max([-5, -1, -8, -2]))

print("==== PROBLEM 2: Count Even Numbers===")
def counting_even(numbers):
    return sum(1 for x in numbers if x % 2 ==0)

print(counting_even([1, 2, 3, 4, 5, 6]))
print(counting_even([10, 15, 22, 33, 44]))

print("===PROBLEM 3: Reverse a List===")
def reverse_in_list(numbers):
    left,right = 0,len(numbers) -1
    while left < right:
        numbers[left],numbers[right] = numbers[right],numbers[left]
        left +=1
        right -= 1
    return numbers
my_list = [1, 2, 3, 4, 5]
reverse_in_list(my_list)
print(my_list)

print("===PROBLEM 4: Remove Duplicates===")
def remove_duplicates(numbers):
    return list(set(numbers))
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
print(remove_duplicates([10, 10, 10]))

print("===PROBLEM 5: Find minimum===")
def find_min(numbers):
    min_val =numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

print(find_min([5, 2, 9, 1, 7, 3]))  # Must print 1
print(find_min([-5, -2, -9, -1])) # Must print -9
