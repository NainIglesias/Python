email = input("Enter email: ")
changedEmail = ""
for char in email:
	if(char == "@"):
		changedEmail += "@ceu.es"
		break
	changedEmail += char
print(changedEmail)
