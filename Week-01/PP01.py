#Get the name of the employee
#Get basic pay 1000
#Get the deductions
#Calculate total pay
#Display name and total pay

name = input("Enter Employee Name: ")
BP = int(input("Enter Basic Pay: "))
DED = int(input("Enter Deduction Amount: "))
TP = BP - DED

print(name, "the total pay is", TP)