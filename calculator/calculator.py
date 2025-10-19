import art

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    if n2!=0:
        return n1/n2
    else:
        return "Cannot Divide by 0"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(art.logo)
n1=float(input("Enter the First Number: "))
should_accumulate=True

while should_accumulate:
    op=input("Enter operation to be performed + - * / : ")
    n2=float(input("Enter Second Number: "))

    ans = operations[op](n1,n2)
    print(f"{n1} {op} {n2} = {ans}")
    ques = input("Do you want to keep going? y or n: ")
    if ques=='y':
        should_accumulate=True
        n1=ans
    else:
        should_accumulate=False