def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

try:
    a = input("Enter Fibonacci sequence index: ")
    value = int(a)
    print(fibonacci(value))
except:
    print("Input must be a number!")

