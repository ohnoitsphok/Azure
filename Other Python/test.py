while True:
    m = (input("Nhap so: "))
    if m == "Stop" or m == "stop":
        break
    def sumOfAll(n):
        total = 0
        total = n % 10
        n = int(n/10)
        total = total + n
        return total
    n = int(m)
    print(sumOfAll(n))