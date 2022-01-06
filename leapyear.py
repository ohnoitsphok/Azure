m = int(input("Input month: "))
y = int(input("Input year: "))

def feb(year):
    if year % 4 == 0:
        print("Month has 29 days")
    else:
        print("Month has 28 days")

if m in [1, 3, 5, 7, 8, 10, 12]:
    print("Month has 31 days")
elif m in [4, 6, 9, 11]:
    print("Month has 30 days")
elif m == 2:
    if y % 100 == 0:
        if y % 400 == 0:
            feb(y)
        else:
            print("Month has 28 days")
    else:
        feb(y)
else:
    ("Month does not exist.")