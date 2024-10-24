''' ORIGINAL CODE
for x :
        print("*")
        print("**")
        print("***")
        print("****")

Your Challenge:
Fix the for loop to be a for loop in range(), starting at 0 and ending at 6, incrementing by 1.
Create your first conditional statement that checks if x is equal to 0 or equal to 6, and print out one asterisk if so. 
Create an elif statement that checks if x is equal to 1 or x is equal to 5, and print out two asterisks if so. 
Create another elif statement that checks if x is equal to 2 or equal to 3, and prints out three asterisks if so.
Create one last else statement that prints out four asterisks. 
'''

for x in range(0, 6, 1):
        if x == 0 or x == 6:
                print("*")
        elif x == 1 or x == 5:
                print("**")
        elif x == 2 or x == 3:
                print("***")
        else:
                print("****")

''' OUTPUT:
*
**
***
***
****
**
'''