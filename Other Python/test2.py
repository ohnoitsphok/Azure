lst = []
while True:
    while True:
        try:
            a = input("Nhap so: ")
            if a == "find":
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

    while True:
        try:
            b = input("Find: ")
            findNum = int(b)
            break
        except:
            print("Input must be a number!")
            continue

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
        print("Number is at " + str(binarySearch(lst, findNum)) + " in list")
    else:
        print("Number not in list")
        break