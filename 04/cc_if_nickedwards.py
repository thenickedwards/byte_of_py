"""
  Students  |  Grades  |  Letters
------------|----------|----------
  George    |  46      |  F
  Michell   |  80      |  B
  Josh      |  12      |  F
  Chloe     |  68      |  D
  Stanley   |  99      |  A
  Annie     |  100     |  A+
"""
gradeToTest = 0
if gradeToTest == 100:
    print("A+")
elif gradeToTest >= 90:
    print("A")
elif gradeToTest >= 80:
    print("B")
elif gradeToTest >= 70:
    print("C")
elif gradeToTest >= 50:
  print("D")
else:
  print("F")


'''
Note: this was an exercise for practice though this code could be improved.
The program should check the input to insure the number valid and
throw an error if invalid input is submimtted 
(e.g. not a number, values too high, values too low, integers/floats, etc)
'''