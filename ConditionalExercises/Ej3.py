def divisionnCero(n1,n2):
    try:
        if(n1|n2==0):
            print("ERROR")
        else:
            print(n1/n2)
    except:
        print("ERROR")
number1 = int(input("Write a number: "))
number2 = int(input("Write another number:"))
divisionnCero(number1,number2)