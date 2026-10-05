#Functions are pieces of code that accomplish a specific task

#input() - #gets input from user
#print() - #displays screen
#list.append()
#exit()
#list.sorted()
#remove()
#int()
#str()
#dictionary.update()


#User Defined Functions
#    def add():
#       a = input()
#        b = input()
#        c=a+b
#        print(c)

## Main Code
def add():
    a= int(input("Enter value a: "))
    b= int(input("Enter value b: "))
    c=a+b
    print(c)
def subtract():
    a= int(input("Enter value a: "))
    b= int(input("Enter value b: "))
    c=a-b
    print(c)
def multiply():
    a= int(input("Enter value a: "))
    b= int(input("Enter value b: "))
    c=a*b
    print(c)
def divide():
    a= int(input("Enter value a: "))
    b= int(input("Enter value b: "))
    c=a/b
    print(c)

while (1):
    print("1 Add")
    print("2 Subtract")
    print("3 Multiply")
    print("4 Divide")
    print("5 Exit")
    select = int(input("Enter your choice: "))
    if select == 1:
        add()
    elif select == 2:
        subtract()
    elif select == 3:
        multiply()
    elif select == 4:
        divide()
    elif select == 5:
        exit()