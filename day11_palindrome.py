print("===palindrome===")
def is_palindrome(s):
    cleaned = ""

    for char in s:
        # FILL IN THE BLANK: Check if char is a letter or number
        if char.isalnum():
            # FILL IN THE BLANK: Add lowercase version of char to cleaned
            cleaned = cleaned+ char.lower()

    # FILL IN THE BLANK: Check if cleaned is equal to its reverse
    return cleaned == cleaned[::-1]

# === TEST CASES (Do not change these) ===
print(is_palindrome("A man, a plan, a canal: Panama"))  # Expected: True
print(is_palindrome("race a car"))                      # Expected: False
print(is_palindrome(" "))                               # Expected: True