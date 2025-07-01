"""
#*************DAY 1*************
#Trafic Light
light = input("Light : ")
if (light == "red"):
    print("STOP")
elif(light == "green"):
    print("GO")
elif(light == "yellow"):
    print("READY")
else:
    print("Some Issue")

#Sum two integer numbers
num1= int (input("Enter number1: "))
num2= int (input("Enter number2: "))
sum= (num1+num2)
print("Sum of", num1, "and", num2, "is", sum)

#Calculate area of square
side= int (input("Enter length of square: "))
area= side**2
print (f"Area: {area}")

#Average of two integer numbers
num1= float(input("Enter 1st number: "))
num2= float(input("Enter 2nd number: "))
sum= num1+num2
avg= sum/2
print(f"Average is: {avg}")

#Print True if a is greater than b else print False
a= int(input("Number1: "))
b= int(input("Number2: "))
if a>=b:
    print("True")
else:
    print("False")

#*************DAY 2*************
str= "atqa asma"
print (str[2: 6])
print(str.endswith("ma"))
str=str.capitalize()
print(str)
print(str.replace("as", "As"))
print(str.count("a"))
print(str.find("a"))


#WAP to input users first name and print its lenght
first_name= input("Enter name: ")
lenght= len(first_name)
print(f"Lenght of string is: {lenght}")


#WAP to find occurance of "$" in string
str1= "1$234$67@&"
str1count=str1.count("$")
print(f"No. of times $ occured in \"{str1}\" is {str1count}")

#Grade students base don marks
marks= int(input("Enter marks: "))
if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=80 and marks<90:
    print("Grade: B")
elif marks>=70 and marks<80:
    print("Grade: C")  
elif marks<70 and marks>=0:
    print("Grade: B")  
else :
    print("Invalid")     

#WAP to check if the number entered by user is even or odd
number= int(input("Enter number: "))
if ((number % 2) == 0):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")    

#WAP to find greatest of three numbers
num1= int(input("Enter number 1: "))
num2= int(input("Enter number 2: "))
num3= int(input("Enter number 3: "))
if num1>num2 and num1>num3:
    greatest= num1
elif num2>num1 and num2>num3:
    greatest= num2
elif num3>num1 and num3>num2:
    greatest= num3
print(f"Greatest among {num1} {num2} {num3} is {greatest}")    
"""

#WAP to check if the number is multiple of 7.
num= int(input("Enter number: "))
rem=num%7
if (rem==0)



