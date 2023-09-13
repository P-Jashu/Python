from art import logo
from replit import clear

def add(n1, n2):
    return (n1+n2)

def sub(n1, n2):
    return (n1-n2)

def mul(n1, n2):
    return (n1*n2)

def div(n1, n2):
    return (n1/n2)

def cal():
    print(logo)

    n1 = float(input("Enter the number: "))
    operations = {
        "+" : add,
        "-" : sub,
        "*" : mul,
        "/" : div
    }

    for i in operations:
        print(i)
    cal_continue = True
    
    while cal_continue:

        op = input("Enter your prefered operation:")
        n2 = float(input("Enter number: "))
        ans = operations[op](n1,n2)
        print(f"{n1} {op} {n2} = {ans}")
        option = input("Do you want to cantinue calculating(y or n): ")

        if (option == "y"):
            n1 = ans
        else:
            cal_continue = False
            clear()
            cal()

cal()
