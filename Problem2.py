# Write a program to fill name and date entered by the user

name = input("Enter name : ")
date = input("Enter date : ")

print("Hello",name,"Congratulations You are selected as an employee in Capgemini your joining date is",date)

print(f"Hello {name} Congratulations You are selected as an employee in Capgemini your joining date is {date}")

letter = '''Dear |<Name>| you are selected congratulations
 Your joining date is |<Date>|'''

print(letter.replace("|<Name>|", "Manasi").replace("|<Date>|","26/12/2024"))