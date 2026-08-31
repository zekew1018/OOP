Course1 = int(input("Enter Student Course 1 Grade: "))
Course2 = int(input("Enter Student Course 2 Grade: "))
Course3 = int(input("Enter Student Course 3 Grade: "))

if Course1 > 100 or Course2 > 100 or Course3 > 100:
    print("Invalid Grade")
    exit()
if Course1 < 0 or Course2 < 0 or Course3 < 0:
    print("Invalid Grade")
    exit()

TotalGrade = (Course1 + Course2 + Course3)
PercentageGrade = (TotalGrade / 300)*100

if PercentageGrade == 100:
    print("Percentage Grade is 100, Grade A")
elif PercentageGrade < 100 and PercentageGrade >= 90:
    print("Grade A")
elif PercentageGrade < 90 and PercentageGrade >= 80:
    print("Grade B")
elif PercentageGrade < 80 and PercentageGrade >= 70:
    print("Grade C")
elif PercentageGrade < 70 and PercentageGrade >= 60:
    print("Grade D")
elif PercentageGrade < 60 and PercentageGrade >= 0:
    print("Grade F")

print("Percentage Grade: ", PercentageGrade)