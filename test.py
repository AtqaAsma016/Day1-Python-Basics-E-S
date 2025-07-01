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
# 3456
