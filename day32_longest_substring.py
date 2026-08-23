print("===longest_substring===")
def length_of_longest_substring(s):
    char_index = {}
    left = 0
    max_len = 0
    for right in range(len(s)):
        char = s[right]
        if char in char_index:
            if char_index[char] >= left:
                left = char_index[char] +1
        char_index[char] = right
        current_len = right - left +1

        if current_len > max_len:
            max_len = current_len

    return max_len

print(length_of_longest_substring("abcabcbb"))  # Expected: 3
print(length_of_longest_substring("bbbbb"))     # Expected: 1
print(length_of_longest_substring("pwwkew"))    # Expected: 3