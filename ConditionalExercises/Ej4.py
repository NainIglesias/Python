def isEven(number):
    return number%2==0;
def printEven(even):
    if(even):
        print("ES PAR")
    else:
        print("ES IMPAR")
number = int(input("Write a number:"))
printEven(isEven(number))