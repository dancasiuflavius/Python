def is_palindrome(word):
    return word == word[::-1]

word = input("Introdu un cuvânt: ")

if is_palindrome(word):
    print("Este palindrom")
else:
    print("Nu este palindrom")
