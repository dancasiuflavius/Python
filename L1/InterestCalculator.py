principal = float(input("Introdu suma principală: "))
rate = float(input("Introdu rata anuală a dobânzii (de ex. 5, 6, 10): "))
time = float(input("Introdu timpul în ani: "))

interest = (principal * rate * time) / 100

print("Dobânda calculată este:", interest)
