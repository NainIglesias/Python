def groupA(name,gender):
    if(gender == "M" and name[0] <= 'M'):
        return True
    elif(gender == "H" and name[0] >= 'N'):
        return True
    else:
        return False
def printGroupA(group):
    if(group):
        print("Group A")
    else:
        print("Group B")
gender = input("Gender '(H,M)':")
name = input("Name:")
printGroupA(groupA(name, gender))