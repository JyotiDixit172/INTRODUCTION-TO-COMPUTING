# Question 1
str1="Python is a case sensitive language" 
print("<A>length og string is:",len(str1)) #to find the length of string
print("<B>Reversed String is:",str1[::-1])
str2=str1[10:26] #storing case sensitive in new string
str2.replace("a case sensitive","object oriented") # "a case sensitive" REPLACED BY "object oriented"
print("<E>The index of substring a is ",str1.find('a'))
print("<F>The original string after removing whitespaces is",str1.replace(" ",""))
print("\n")


#Question 2
Name=input("ENTER YOUR NAME:")
SID=int(input("ENTER YOUR SID:"))
Department=input("ENTER YOUR DEPARTMENT:")
CGPA=float(input("ENTER YOUR CGPA:"))
print("Hey %s,"%Name,"Here!")
print("My SID is %d" %SID)
print("I am from %s"%Department,"and my CGPA is %f"%CGPA)
print("\n")

#Question 3
a=60
b=20
print("a. ",a&b)
print("b. ",a|b)
print("c. ",a^b)
print("Left shift both a and b with 2 bits are :",a<<2 ,b<<2)
print("Right shift a with 2 bits and b with 4 bits are : ",a>>2,b>>4)
print("\n")


#Question 4
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
 
if (num1 >=num2) and (num1 >=num3):
   largest = num1
elif (num2 >=num1) and (num2 >=num3):
   largest = num2
else:
   largest = num3
 
print("THE LARGEST NUMBER IS ",largest)
print("\n")



#Question 5
s=input("ENTER A STRING:")
if 'name' in s:
    print ("YES")
else:
    print ("NO")
print("\n")


#Question 6
a=float(input("ENTER FIRST SIDE OF TRIANGLE:"))
b=float(input("ENTER SECOND SIDE OF TRIANGLE:"))
c=float(input("ENTER THIRD SIDE OF TRIANGLE:"))
if(a>=(b+c)):      #Equality sign used as if sum of two sides is equal to third then triangle is not valid
    print("No")
elif(b>=(a+c)):
    print("No")
elif(c>=(a+b)):
    print("No")
else:
    print("Yes")    


