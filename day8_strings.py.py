print("===excersise 1===")
name = "yathin"
print("starting letter is:" , name[0])
print("second letter is:" , name[1])
print("last letter is:" , name[5])
print("ending letter is:" , name[-1])

print("===excersise 2===")

word = "kakarla"
print("word:" , word)
print("letter 0 to 3" , word[0:4])
print("letter 1 to 4" , word[1:5])
print("letter 0 to 6" , word[:7])
print("letter o to 6" , word[0:])

print("===excersise 3===")

word = "hii yathin"
print("original:" , word)
print("length:" , len(word))
print("word with lower class:" , word.lower())
print("word with upper class:" , word.upper())
print("woed with no space:" , word.strip())
print("replace 'guys' with 'yathin':" , word.replace("yathin","guys"))

print("===excersise 4===")
sentence = "i love working hard"
words = sentence.split(" ")
print("sentence:" , sentence)
print("seperate words:" , words)
print("first letter:" , sentence[0])
print("last letter:", sentence[-1])

joined_back = " ".join(words)
print("joined words:" , joined_back)

print("===excersise 5===")
message = "python is easy.i use python"
print("message:", message)

pos = message.find("easy")
print("where is the word easy:" , pos)

count = message.count("python")
print("'python' appears:" , count , "times")

print("===excersise 6===")
def is_palindrome(text):
    cleaned = text.strip().lower()
    reversed_text = cleaned[::-1]
    return cleaned == reversed_text

test1 = "amma"
test2 = "yathin"
test3 = "dad"

print(test1 , "is_palindrome?" , is_palindrome("amma"))
print(test2 , "is_palindrome?" , is_palindrome("yathin"))
print(test3 , "is_palindrome?" , is_palindrome("dad"))

print("===excersiser 7===")
def is_anagram(word1,word2):
    clean1 = word1.replace(" ","").lower()
    clean2 = word2.replace(" ","").lower()

    return sorted(clean1) == sorted(clean2)

print("'listen' and 'silent' are anagrams?" , is_anagram("listen","silent"))
print("'hello' and 'hii' are anagrams?" , is_anagram("hello","hii"))