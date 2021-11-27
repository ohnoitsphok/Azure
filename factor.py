def factorial(a):
    if a < 0:
        print("Invalid")
    elif a <= 1:
        return 1
    else:
        return a*factorial(a-1) 

def inputNumber():
    while True:
        try: 
            a = int(input("Enter factorial: "))
            print(factorial(a))
            break
        except:
            print("Input must be a number")
            continue

inputNumber()