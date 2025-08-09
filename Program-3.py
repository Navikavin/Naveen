a = int(input("7: "))

terms = a if a % 2 != 0 else a - 1

for i in range(terms):
    print(2 * i + 1, end=", " if i < terms - 1 else "")
