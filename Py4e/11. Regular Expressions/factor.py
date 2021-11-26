num = 1
def factorial(num, a):
    if a < 0:
        print("Invalid")
    elif a == 0:
        return 1
    else:
        for value in range(1, a + 1):
            num = num * value
        return num
        
try: 
    a = int(input("Enter factorial: "))
    print(factorial(num, a))
except:
    print("Input must be a number")
