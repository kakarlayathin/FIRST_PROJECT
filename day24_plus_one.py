print("===plus_one===")
def plus_one(digits):
    i = len(digits)-1
    while i >=0:
        if digits[i] < 9:
            digits[i] = digits[i] +1
            return digits
        else:
            digits[i] = 0
            i = i -1
    return [1] + digits

print(plus_one([1, 2, 3]))   # Expected: [1, 2, 4]
print(plus_one([4, 3, 2, 1])) # Expected: [4, 3, 2, 2]
print(plus_one([9]))         # Expected: [1, 0]
print(plus_one([9, 9]))      # Expected: [1, 0, 0]