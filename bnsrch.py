def program():
    lst = []
    while True:
        while True:
            try:
                a = input("Nhap so: ")
                if a == "find" or a == "Find":
                    break
                elif a == "reset" or a == "stop":
                    break
                n = int(a)
                if n not in lst:
                    lst.append(n)
                else:
                    print("Number already existed in list")
                    continue
            except:
                print("Input must be a number")
                continue

        if a == "reset" or a == "stop":
            break

        while True:
            try:
                b = input("Find: ")
                if b == "stop" or b == "reset":
                    break
                findNum = int(b)
                break
            except:
                print("Input must be a number!")
                continue

        if b == "stop" or b == "Reset":
            break

        def binarySearch(list, find):
            bot = 0
            top = len(list) - 1
            mid = 0
            while bot <= top:
                mid = (top + bot) // 2
                if list[mid] < find:
                    bot = mid + 1
                elif list[mid] > find:
                    top = mid - 1
                else:
                    return mid

        lst.sort()

        if findNum in lst:
            print("Number is at " + str(binarySearch(lst, findNum) + 1) + " in list")
            continue
        else:
            print("Number not in list")
            continue

    if a == "reset" or a == "Reset":
        program()

def cmd():
    while True:
        prompt = input("")
        if prompt == "start" or prompt == "Start":
            program()
        elif prompt == "quit" or prompt == "Quit":
            break
        else:
            print("Invalid command!")
            continue
cmd()