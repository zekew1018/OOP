while (1):
    print("1 Area of a Rectangle") # l x w
    print("2 Volume of a Rectangular Cube") # h x w x l
    print("3 Area of a Circle") # 3.14159 * r * r
    print("4 Circumference of a Circle") # 2 * 3.14159 * r
    print("5 Quit")
    select = input("Enter your choice: ")
    if select == "5":
        print("Thank you for using The Somewhat-Practical Calc!")
        exit()
#I understand that the code isn't very efficient, I prefer the situational dialogue if that makes sense.
    if select == "1":
        print("You've selected 'Area of a Rectangle'")
        l = float(input("Enter the width of the rectangle: "))
        w = float(input("Enter the length of the rectangle: "))
        a = w * l
        print("The area of the rectangle is", a, "units^2.")
    elif select == "2":
        print("You've selected 'Volume of a Rectangular Cube'")
        h = float(input("Enter the height of the cube: "))
        l = float(input("Enter the width of the cube: "))
        w = float(input("Enter the length of the cube: "))
        a = w * l * h
        print("The volume of the cube is", a, "units^3.")
    elif select == "3":
        print("You've selected 'Area of a Circle'")
        r = float(input("Enter the radius of the circle: "))
        a = (r * r) * 3.14159
        print("The area of the circle is", a, "units^2.")
    elif select == "4":
        print("You've selected 'Circumference of a Circle'")
        r = float(input("Enter the radius of the circle: "))
        a = 2 * 3.14159 * r
        print("The area of the circle is", a, "units^2.")