def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input("Introdu un număr întreg: "))
print(f"Factorialul lui {n} este {factorial(n)}")
