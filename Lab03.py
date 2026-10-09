b = 100000
myBooks = {}
def add_book():
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    pubYear = int(input("Enter Publication Year: "))
    myBooks.update({"Book"+str(b): {
        "Title":title,
        "Author":author,
        "Year of Publication":pubYear}})
def delete_book():
    print(myBooks)
    delCheck = input("Enter BookID: ")
    if delCheck in myBooks:
        del myBooks[delCheck]
def book_Menu():
    print("1. Add Book")
    print("2. Delete Book")
    print("3. Display Library")
    print("4. Exit")

#---------------------------------------------------------------------------------------------------
u = 100000
myUsers={}
def add_User():
    name = input("Enter Name: ")
    password = input("Enter Password: ")
    address = input("Enter Address: ")
    phone = int(input("Enter Phone Number: "))
    email = input("Enter Email Address: ")
    myUsers.update({"User"+str(u): {
        "User":name,
        "Password":password,
        "Address":address,
        "Phone":phone,
        "Email":email}})
def delete_User():
    print(myUsers)
    delCheck = input("Enter UserID: ")
    if delCheck in myUsers:
        del myUsers[delCheck]
def user_Menu():
    print("1. Add User")
    print("2. Delete User")
    print("3. Display Users")
    print("4. Exit")
#---------------------------------------------------------------------------------------------------
a = 100000
myAuthors={}
def add_Author():
    name = input("Enter Name: ")
    affiliation = input("Enter Affiliation: ")
    country = input("Enter Country: ")
    phone = int(input("Enter Phone Number: "))
    email = input("Enter Email Address: ")
    myAuthors.update({"Author"+str(a): {
        "User":name,
        "Affiliation":affiliation,
        "Country":country,
        "Phone":phone,
        "Email":email}})
def delete_Author():
    print(myAuthors)
    delCheck = input("Enter AuthorID: ")
    if delCheck in myAuthors:
        del myAuthors[delCheck]
def author_Menu():
    print("1. Add Author")
    print("2. Delete Author")
    print("3. Display Authors")
    print("4. Exit")
#---------------------------------------------------------------------------------------------------
def menu():
    print("Please select a Category:")
    print("1. Books")
    print("2. Users")
    print("3. Authors")
    print("4. Exit")
while True:
    menu()
    select = int(input("Enter Select Option: "))
    if select == 1:
        book_Menu()
        bSelect = int(input("Enter Select Option: "))
        if bSelect == 1:
          add_book()
          b = b+1
        if bSelect == 2:
            delete_book()
        if bSelect == 3:
            print(myBooks)
        if bSelect == 4:
                menu()
    if select == 2:
        user_Menu()
        uSelect = int(input("Enter Select Option: "))
        if uSelect == 1:
            add_User()
            u = u+1
        if uSelect == 2:
            delete_User()
        if uSelect == 3:
            print(myUsers)
        if uSelect == 4:
            menu()
    if select == 3:
        author_Menu()
        aSelect = int(input("Enter Select Option: "))
        if aSelect == 1:
            add_Author()
            a = a+1
        if aSelect == 2:
            delete_Author()
        if aSelect == 3:
            print(myAuthors)
            menu()
    if select == 4:
        exit()
