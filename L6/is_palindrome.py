def is_palindrome(text: str) -> bool:
    text = "".join(c.lower() for c in text if c != " ")
    return text == text[::-1]


# Teste
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("ana"))                          # True
print(is_palindrome("Ana are mere"))                 # False
print(is_palindrome(""))                             # True
print(is_palindrome("   "))                          # True
