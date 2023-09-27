#Asks user for the first name
FirstName = input("Whats Your First Name? ")
#Asks user for middle name
MiddleName = input("Whats Your Middle Name? ")
#Asks user for last name
LastName = input("Whats Your Last Name? ")

#Prints Name Together
print("Your Name is,", FirstName , LastName,", Right?")
#Prints Out Initials
print('Your Intials Are, '+
      FirstName.upper()[0],     #Grabbng the first letter of the first name, then converting it to uppercase
      MiddleName.upper()[0],     #Grabbng the first letter of the middle name, converting it to uppercase
      LastName[0].upper()+      #Getting The first letter of the last name and converting it to uppercase
      LastName[1:].lower()      #Using the slicing function we get the rest of the letters starting from the seccond letter lowercase
      )


if MiddleName == "":
    