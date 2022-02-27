print("Answer 1\n")
def Tower_Hanoi(n , rod_1, rod_2, rod_3):
	if n == 0:
		return
	Tower_Hanoi(n-1, rod_1, rod_3, rod_2)
	print("Move disk",n,"from rod",rod_1,"to rod",rod_2)
	Tower_Hanoi(n-1, rod_3, rod_2, rod_1)
n = 3
Tower_Hanoi(n, 'A', 'C', 'B')
print("\n")

#QUESTION 2
print("ANSWER 2\n")
from math import factorial, remainder
n=int(input("Enter size of PASCAL's triangle: "))

print(" BY USING FOR LOOP\n ")

for a in range(n):
	for j in range(n-a+1):
		print(end=" ")                          # for spacing

	for j in range(a+1):
		print(factorial(a) // (factorial(j)*factorial(a-j)), end=" ")	# nCr = n!/((n-r)!*r!)
	print()	                                        # for new line
print("\n\n")

print(" BY USING WHILE LOOP\n ")
i=0
while(i<n):
    z=n-i+1
    while(z>0):
        print(end=" ")
        z-=1
    y=0
    while(y<i+1):
        print(factorial(i) // (factorial(y) * factorial(i - y)), end=" ")
        y+=1
    i+=1
    print()
print("\n\n")

print(" BY USING RECURSION METHOD\n ")

def pascal_tri(n,originalength=n):
    if n == 0:
        return
    pascal_tri(n-1,originalength)
    print('  '*(originalength-n), end='')   # Printing the spaces.

      
    start = 1                               # first number is always 1.
    for i in range(1, n+1):
        print(start, end ='   ')
        start = start * (n - i) // i        # using Binomial Coefficient.
    print()
pascal_tri(n)
print("\n")




#QUESTION 3
print("ANSWER 3\n")
int1, int2 = map(int,input("Enter 2 numbers with space ONLY: ").split())
Quotient = int1 // int2
Remainder = int1 % int2

#part (a)
print("part_(a). Checking if quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))

#part (b)
if (Quotient == 0):
    print("part_(b)  Quotient is zero")
if (Remainder == 0):
    print("part_(b) Reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print("part_(b)  All the values are non_zero")

#part_(c)
part_C_list = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(part_C_list)):
    if part_C_list[i] > 4:
        result.append(part_C_list[i])
print(f"part_(c) Filtered values which are greater than 4 are : {result}")

#part (d)
set_result = set(result)
print("part_(d) Set:",set_result)

#part (e)
immutable_Set = frozenset(set_result)            # Frozen Set is used to make the set immutable.
print("part_(e) Immutable set is: ",immutable_Set)

#part (f)
print("part_(f) Hash value of the max value from the above set:", hash(max(immutable_Set)))
print("\n")

#QUESTION 4
print("ANSWER 4\n")
class Student:
    def __init__(self, student,roll_no):
        self.name = student
        self.roll_no = roll_no
    
    def __del__(self):
        print("Object is now destroyed.")                   

student_1 = Student("JYOTI", 21103013)              # creating object.
print("Object created.")
print(f"The name of the student it {student_1.name} and SID is {student_1.roll_no}.")    # printing the assigned values.
del student_1                                       # deleting object.
print("\n")

#QUESTION 5
print("ANSWER 5\n")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
employee_1 = Employee("Mehak", 40000)               # creating record of EMPLOYEES.
employee_2 = Employee("Ashok", 50000)
employee_3 = Employee("Viren", 60000)


employee_1.salary = 70000                           # part_(a) updating the salary.
print(f"<a> The updated salary of {employee_1.name} is {employee_1.salary}. ")

print("<b> Viren's record is deleted now.", end='') # part_(b) deleting a record.
del employee_3
print("\n")

#QUESTION 6
print("ANSWER 6\n")
word =input("Enter the word: ")   # Prompting the FIRST FRIEND to enter a word.
word=word.lower()

#Prompting the SECOND FRIEND to make a new meaningful word using exact same Alphabets from word entered by FIRST FRIEND's .

test_word = input("Enter a new MEANINGFUL WORD using same ALPHABETS to test your FRIENDSHIP: ") 
test_word=test_word.lower()

def count_in_dict(word):  
    count = {}
    list_1 = list(word)
    
    n = len(list_1)
    for i in range(n):
        if list_1[i] in count:
            count[list_1[i]] += 1
        else:
            count[list_1[i]] = 1
    return count


def check_user_input():       #defining a function to check the wether word is MEANINGFUL or not.
    if count_in_dict(word) != count_in_dict(test_word):
        print("The ALPHABETS of word entered by SECOND FRIEND aren't SAME, so their FRIENDSHIP is FAKE.")
        return
    Ques = input("Is the word MEANINGFUL?(y/Y or n/N): ")

    if Ques == 'y' or Ques=='Y':
        print("The FRIENDS have successfully passed FRIENDSHIP TEST.")
    elif Ques == 'n' or Ques=='N':
        print("Word entered is not MEANINGFUL,FRIENDSHIP is fake.")
    else:
        print("Invalid input,try again with y/Y or n/N.")
        check_user_input()
check_user_input()
