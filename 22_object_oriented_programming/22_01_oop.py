'''
Programming Paradigms
(A way to approach and structure code)
* Procedural
    - great for beginners, step-by-step instructions
    - tasks = modular procedures (e.g. get user input, write to file, perform calculation
    - Other like terms: procedure, routine, subroutine, etc
* Object-Oriented (OOP)
    - Objects: a unit that bundles together related data and executable code
    - Attributes (data) & Methods (executable code)
* Functional
    - Focuses on functions (not procedural)
    - Pure functions, avoidance of side effects, use of immutable data
    - Many programming languages support multi-paradigm programming.
'''


# Object-Oriented Programming
class object_blueprint:
    # instance attributes
    def __init__(self, parameter1, parameter2):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        self.attribute = 1 # default value for object
        self.data_stucutre = "custom"
        self.inheritance = True
    
    def custom_method(self): 
        print("Hello World!")
    
    def update_parameter1(self, new_parameter1):
        self.parameter1 = new_parameter1


''' FOOD 4 THOUGHT ON CLASSES
1. What is the purpose of the __init__ method in a class? When does it execute? 
The __init__ function (called a "constructor") is a native method in Python that defines an object when instantiated with attributes and methods of the class.

2. What is the purpose of the self parameter in a method? 
The self parameter is passed to the method of a class to ensure the attributes of the class are passed along to the method.
(From the web: In Python, the "self" parameter within a method refers to the current instance of the class, allowing the method to access and modify the attributes and methods specific to that particular object being used; essentially, it provides a way for a method to interact with its own data within the class.)

3. What is an instance?
An instance is a data object instantiated by a class that shares the structure and attributes defined by the class but has attributes with values unique to itself.

?. What is inheritance?
Inheritance allows a developer to create a structure of class objects based on one another--with parent classes (sometimes called superclasses) and child classes (sometimes called subclasses) which can inherit and/or overwrite the values of attibutes and methods.

4. How do you define a subclass from a superclass?
A subclass is a blueprint for a data object which inherits some or all of the attributes and methods of the superclass.

5. What is the use of the super() function?
The super() function incorporates the attributes and methods from a bse class/superclass into a subclass, otherwise those values will not be part of the subclass.
'''
