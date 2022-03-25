def fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def inputNumber():
    while True:
        try:
            a = input("Enter Fibonacci sequence index: ")
            value = int(a)
            print(fibonacci(value))
            break
        except:
            print("Input must be a number!")
            continue

inputNumber()        
