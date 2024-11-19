# creating a function
def php_function(): #function declaration--start
    #body of the function
    print("Hello php class students")
# php_function() #calling the function

# create a simple function to calculate the sum of two numbers
def CalcSum():
    # global num1 #how to make a local variable global
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    print(f"The sum of two numbers is {num1+num2}")
# CalcSum()
# print(num1) #the local variable can now be used outside the function

name=input("Enter your name: ")
age=input("Enter your age: ")
gender=input("Enter your gender: ")

def personal_details(name, age, gender):
  
    print(f"Hello {name}, happy {age} birthday")

personal_details(name,age,gender)



def substract(a, b):
    result=a-b
    print(f"{a} - {b}={result}")



 