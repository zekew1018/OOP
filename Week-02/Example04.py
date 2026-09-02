while (1):
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("5 Quit")
    select = input("Enter your choice: ")
    if select == "5":
        print("Thank you for using The Inefficient Calc!")
        exit()
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    if select == "1":
        c = a + b
        print("The sum of", a, "+", b, "=",c)
    elif select == "2":
        c = a - b
        print("The sum of", a, "-", b, "=", c)
    elif select == "3":
        c = a * b
        print("The sum of", a, "x", b, "=", c)
    elif select == "4":
        c = a / b
        print("The sum of", a, "/", b, "=", c)
    elif select == "5":
        print("Thank you for using The Inefficient Calc!")
        exit()