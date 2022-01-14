#Assignment 1 CSE_21103013_JYOTI DIXIT

#Ques 1

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
avg= (num1+num2+num3)/3
print("The average of these three numbers is: \n",avg)

#######################################

#Ques 2

Gross_Income = int(input("Enter your gross income(in Dollars):"))
No_of_Dependants = int(input("No. of total dependants:"))

#All values are in dollars
Standard_deduction = 10000
Dependant_deduction = 3000
Tax_Rate = 0.20

Taxable_Income = Gross_Income - Standard_deduction - Dependant_deduction*No_of_Dependants
Tax = Taxable_Income*Tax_Rate

if Tax<0:
    Tax = 0


print("Your income tax is:",Tax)

#######################################

#Ques 3

SID = int(input("Enter SID: \n"))
Name = input("Enter your name: \n")
Gender = input("Enter your Gender(M,F,U for unknown): \n")
Stream = input("Enter your stream: \n")
CGPA = float(input("Enter your CGPA: \n"))

Student = [SID, Name, Gender, Stream, CGPA]

print(Student)

#####################################

#Ques 4

M1 = int(input("Marks of first student: \n"))
M2 = int(input("Marks of second student: \n"))
M3 = int(input("Marks of third student: \n"))
M4 = int(input("Marks of fourth student: \n"))
M5 = int(input("Marks of fifth student: \n"))

Marks = [M1, M2, M3, M4, M5]
print(Marks)

Marks.sort()

print(Marks)

#####################################

#Ques 5(a)

colour = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

colour.pop(3)

print(colour)



#Ques 5(b)

colour = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(colour)

colour[3:5] = ['Purple']
print("new upadated colour list: \n")
print(colour)







