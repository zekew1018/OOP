#Implement all operations of a queue using a List
myQueue = ["John1", "John2", "John3", "John4", "John5"]
def enqueue():
    add = input("Enter name: ")
    myQueue.append(add)
    print("Enqueued successfully.")
def dequeue():
    myQueue.pop(0)
    print("Dequeued successfully.")
def menu():
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
def queue():
    print(myQueue)
while True:
    menu()
    select = int(input("Enter your choice: "))
    if select == 1:
        enqueue()
    if select == 2:
        dequeue()
    if select == 3:
        queue()
    if select == 4:
        exit("Thank you for using this program.")