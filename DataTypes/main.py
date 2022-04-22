# String Concatination
firstName = input("Enter first name")
lastName = input("Enter last name")
dateOfBirth = input("Enter date of birth")
gender = input("Enter the gender")
address = input("Enter the Address")
print("Hi" + " " + firstName + lastName + "How are you?")
print("We will send you Birthday gift to you on" + " " +  dateOfBirth) 
print("please find the gift at" + " " + address)


# f-string
firstName = "sowmya"
lastName = "bondili"
age = 25
grade = 9.8
print(f"Hello {firstName}.{lastName} you are {age} years old. you got {grade} in your graduation")

# String-Length calculation
name = input("enter the name")
length = len(name)
print("it has" + " "  + str(length) + " " + "characters")
print(f"it has {length} characters")
