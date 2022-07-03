while True:
    try:
        user_1 = int(input("Enter number 1: "))
        user_2 = int(input("Enter number 2: "))
        s = user_1 + user_2
        print(s)
        break
    except:
        print("ValueError!!!")
