#ANSWER_1
print("Answer_1\n")
a=str(input("ENTER ANY STRING: "))
list=a.split()                        # Splitting all elements of string in a list
d1={}                               # initializing an empty dictionary named d1
if list.__len__()==1:             # if statement will execute when ONLY a single word is entered
    for i in list[0]:
        if i in d1:
            d1[i]+=1
        else:
            d1[i]=1
    print(d1)   
else:                             # else statement will execute when MORE than one word is entered in a string
    for i in list:
        if i in d1:
            d1[i]+=1
        else:
            d1[i]=1
    print(d1)
print("\n")


#ANSWER_2
print("Answer_2\n")
def next_date():
    L1=[1,3,5,7,8]              
    L2=[4,6,9,11]
    L3=[2]
    L4=[12]
    while True:                 
        Day=int(input("ENTER THE DAY: "))
        if 1<=Day<=31:
            break
        else:
            print("OOPS!! Please enter day between 1-31 ONLY")
    while True:                 
        Month=int(input("ENTER THE MONTH: "))
        if 1<=Month<=12:
            break
        else:
            print("OOPS!! Please enter a MONTH between 1-12 ONLY")
    while True:                
        Year=int(input("ENTER THE YEAR: "))
        if 1800<=Year<=2025:
            break
        else:
            print("OOPS!! Please enter a YEAR between 1800-2025 ONLY")
    if Month in L1 :    
        if Day==31:
            Day=1
            Month+=1
            print(Day,"/",Month,"/",Year)
        elif Day<31:
            Day+=1
            print(Day,"/",Month,"/",Year)
        else:
            print("OOPS!! Conditions didn't match. START AGAIN!!")  # when day>31 but month in L1 = [1,3,5,7,8]
            next_date()
    
    elif Month in L2 :
        if Day==30:
            Day=1
            Month+=1  
            print(Day,"/",Month,"/",Year)   
        elif Day<30:
            Day+=1
            print(Day,"/",Month,"/",Year)
        else:
            print("OOPS!! Conditions didn't match. START AGAIN!!") # when day>30 but month in L2 = [4,6,9,11]
            next_date()      
    elif Month in L3:
        if Year % 4 == 0:  
            if Day==29:
                Day=1
                Month+=1
                print(Day,"/",Month,"/",Year)
            elif Day<29:
                Day+=1
                print(Day,"/",Month,"/",Year)
            else:
                print("OOPS!! Conditions didn't match. START AGAIN!!")
                next_date()
        else:
            if Day==28:
                Day=1
                Month+=1
                print(Day,"/",Month,"/",Year)
            elif Day<28:
                Day+=1
                print(Day,"/",Month,"/",Year)
            else:
                print("OOPS!! Conditions didn't match. START AGAIN!!")
                next_date()
    elif Month in L4:
        if Day==31:
            Day=1
            Month=1
            Year+=1  
            print(Day,"/",Month,"/",Year)
        elif Day<31:
            Day+=1;
            print(Day,"/",Month,"/",Year)
        else:
            print("OOPS,conditions didn't match. START AGAIN!!")
            next_date()
        
    else:
        print("OOPS,conditions didn't match. START AGAIN!!")
        next_date()
next_date()
print("\n")


#ANSWER_3
print("Answer_3\n")
inputlist = input('SIMPLY Enter list elements separated by space: ')    # list elements to be given by user
list2 = inputlist.split()        #splitting of list

print('list: ', inputlist)       # print inputlist as new list named list2

for i in range(len(list2)):
    list2[i] = int(list2[i])     # convert each item to int type
sq_list =[(list2[i], list2[i]**2) for i in range(len(list2))]

print(sq_list)
print("\n")


#ANSWER_4
print("Answer_4\n")
def input_grade():
    grade= int(input("Enter your Grade: "))
    if grade>10 or grade<4:                     # check if the grade meets the conditions
        print("Invalid grade!You can only enter a GRADE between 4-10 should be an int.Try Again")
        grade = input_grade()
    return grade
grade=input_grade()
if grade==4:
    print("Grade you entered is: 'D'= POOR performance")
elif grade==5:
    print("Grade you entered is: 'C'= BELOW AVERAGE performance")
elif grade==6:
    print("Grade you entered is: 'C+' = AVERAGE performance")
elif grade==7:
    print("Grade you entered is: 'B' = GOOD performance")
elif grade==8:
    print("Grade you entered is: 'B+' = VERY GOOD performance")
elif grade==9:
    print("Grade you entered is: 'A'= EXCELLENT performance")
else:
    print("Grade you entered is: 'A+' = OUTSTANDING performance")
print("\n")


#Answer_5
print("Answer_5")
x = 6
for i in range(x):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing alphabet
    for j in range(2*(x-i)-1):
        print(chr(65 + j), end='')  #ASCII VALUE OF A=65,B=66,C=67,D=68,E=69,F=70,G=71,H=72,I=73,J=74,K=75
    print()
print("\n")

#Answer_6
print("Answer_6")
SID = int(input("Enter student's SID(should be unique): "))
NAME = input("Enter student's NAME: ")
STUDENT= {SID:NAME}

while True:
    option = input("Do you want to ADD another student's details?(Y or N): ").upper()
    if option == 'Y':
        SID = int(input("Enter another STUDENT'S SID(should be unique): "))
        NAME = input("Enter another STUDENT'S NAME: ")
        STUDENT[SID] = NAME
    elif option == 'N':
        break
    else:
        print('Enter Y or N only!!!')

#part (a). Printing dictionary STUDENT 
print("<PART a>",STUDENT)

#part (b). Sort by NAMES
print("<PART b>",{k:v for k,v in sorted(STUDENT.items(), key= lambda x:x[1])})  #where k=key , v=value

#part (c). Sort by SID
print("<PART c>",{k:v for k,v in sorted(STUDENT.items())})

#part (d). Search a student's NAME from SID.
SID = int(input("Search Name with SID: "))
print("<PART d>",STUDENT[SID])
print("\n")


#Answer_7
print("Answer_7")
def recur_fibo(n):            #  Function to display the Fibonacci sequence
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
no_of_terms=int(input("ENTER NUMBER OF TERMS IN REQUIRED IN FIBONACCI SERIES: "))
if no_of_terms <= 0:               # Check if the number of terms is valid
   print("Plese enter a positive integer")
else:
   print("The Fibonacci sequence is:")
   sum=0
   for i in range(no_of_terms):
       print(recur_fibo(i))
       sum=sum+recur_fibo(i)
avg=float(sum/no_of_terms)          # CALCULATING THE AVERAGE THE OF FIBONACCI SEQUENCE
print("AVERAGE OF FIBONACCI SERIES IS:",avg)


#Answer_8
print("Answer_8")
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
# part a
Set_Union = Set1.union(Set2)
Set_Intersection = Set1.intersection(Set2)
Part_A_Set = Set_Union - Set_Intersection
print("<PART a>", Part_A_Set)

# part b(Subtracting intersection of sets taken two at a time from the Union of all three sets)
Part_B_Set = Set1.union(Set2.union(Set3)) - Set1.intersection(Set2) - Set2.intersection(Set3) - Set3.intersection(Set1)
print("<PART b>", Part_B_Set)

# part c(Subtracting the intersection of all three sets from the Intersection of sets taken two at a time)
Part_C_Set=((Set1.intersection(Set2)).union((Set1.intersection(Set3)).union(Set2.intersection(Set3))))-(Set1.intersection(Set2.intersection(Set3)))
print("<PART c>",Part_C_Set)
# part d(Excluding the numbers from 1 to 10 that are occuring in Set1)
Part_D_Set = set()
for i in range(1, 11):
    if i not in Set1:
        Part_D_Set.add(i)
print("<PART d>", Part_D_Set)
# part e(Excluding the numbers from 1 to 10 that are occuring in Set1, Set2 and Set3)
Part_E_Set = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        Part_E_Set.add(i)
print("<PART e>", Part_E_Set)
