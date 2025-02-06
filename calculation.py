print("Ankit Patel")
def Addition(x,y):
    return x+y
def Subtraction(x,y):
    return x-y
def Multiply(x,y):
    return x*y
def Divide(x,y):
    return x/y

print("select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Divide")

while True:
    choice=input("Enter Your Choice(1/2/3/4):")
    if choice in ("1", "2","3","4"):
        try:
          num1 = float(input("Enter First Number:"))
          num2 = float(input("Enter Second Number:"))
        except ValueError:
           print("Invalid Input.Please Enter a Number.")
           continue
        if choice == "1":
            print(num1, "+", num2, "=", Addition(num1,num2))
        elif choice == "2":
            print(num1, "-", num2, "=", Subtraction(num1,num2))
        elif choice == "3":
            print(num1, "*", num2, "=", Multiply(num1,num2))
        elif choice == "4":
            print(num1, "/", num2, "=", Divide(num1,num2))
            
            next_calculation = input("Let's do the next calculation? (yes/no):")
            if next_calculation.lower() =="no":
                break
            else:
                print("Invalid Number")