i = 0
myEmployees = {}
def add_employee():
    name = input("Enter Employee Name: ")
    basic_pay = int(input("Enter Basic Pay Amount: "))
    allowance = int(input("Enter Allowance Amount: "))
    deductions = int(input("Enter Deduction Amount: "))
    taxes = int(input("Enter Taxes Amount: "))
    gross_pay = basic_pay + allowance
    net_pay = gross_pay - deductions - taxes
    myEmployees.update({"Employee"+str(i): {
        "Name":name,
        "Basic Pay":basic_pay,
        "Allowance":allowance,
        "Deductions":deductions,
        "Taxes":taxes,
        "Gross Pay":gross_pay,
        "Net Pay":net_pay}})
def delete_employee():
    print(myEmployees)
    delCheck = input("Enter Employee Number: ")
    if delCheck in myEmployees:
        del myEmployees[delCheck]
def mod_employee():
    print(myEmployees)
    modCheck = input("Enter Employee and Number (ex. 'Employee0)': ")
    if modCheck in myEmployees:
        myEmployees[modCheck]["Name"] = input("Enter Employee Name: ")
        modbPay = int(input("Enter Basic Pay Amount: "))
        modAllowance = int(input("Enter Allowance Amount: "))
        modDeductions = int(input("Enter Deduction Amount: "))
        modTaxes = int(input("Enter Taxes Amount: "))
        myEmployees[modCheck]["Basic Pay"] = modbPay
        myEmployees[modCheck]["Allowance"] = modAllowance
        myEmployees[modCheck]["Deductions"] = modDeductions
        myEmployees[modCheck]["Taxes"] = modTaxes
        modGPay = modbPay+modAllowance
        modNPay = modGPay-modDeductions-modTaxes
        myEmployees[modCheck]["Gross Pay"] = modGPay
        myEmployees[modCheck]["Net Pay"] = modNPay
        print("Employee Modified Successfully.")
def menu():
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Display Employee(s) and Information")
    print("4. Modify Employee Information")
    print("5. Exit")

while True:
    menu()
    select = int(input("Enter Select Option: "))
    if select == 1:
        add_employee()
        i = i+1
    if select == 2:
        delete_employee()
    if select == 3:
        print(myEmployees)
    if select == 4:
        mod_employee()
    if select == 5:
        exit()