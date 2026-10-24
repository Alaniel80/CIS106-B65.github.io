#Iana Vasileva  CIS160 B65   M9Ex2    10/24/26
#Write a function that receives the two numbers and uses the operation code to perform an operation on the two numbers
result=0

#define function
def operation(number1, number2, operation_code):
    if operation_code=="A":
        return number1+number2
    elif operation_code=="S":
        return number1-number2
    elif operation_code=="M":
        return number1*number2
    elif operation_code=="D":
        if number2==0:
            return -999
        else:
            return number1/number2
    else:
        print("Please enter a valid operation code")
        exit()

#input
number1=int(input("Enter your first number: "))
number2=int(input("Enter your second number: "))
operation_code=input("Enter your operation code (A,S,M, or D): ").upper()

#compute result
result = operation(number1, number2, operation_code)

#Display results
print("Number 1:",number1)
print("Number 2:",number2)
print("Operation code:",operation_code)
if result==-999:
    print("Invalid operation")
else:
    print("Result:",result)