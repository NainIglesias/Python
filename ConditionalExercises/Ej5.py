def canPayTaxex(age, income):
    return age>16 and income>=1000;
def printTributary(tributary):
    if(tributary):
        print("A pagar impuestos")
    else:
        print("Te libras")
age = int(input("Age:"))
income = int(input("Income:"))
printTributary(canPayTaxex(age,income))