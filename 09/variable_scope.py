# variable dogs in local scope of fucntion
def Seattle():
    dogs = 1000
    print('Seattle has ', dogs, 'dogs.')
    
def Bellevue():
    dogs = 2000
    print('Bellevue has ', dogs, 'dogs.')
    
# global variable can be accessed or modified from anywhere 
# (inside or outside functions)

my_string = "Set in global scope"

def main():
    global my_string
    my_string = "Set in local scope"
    
main()
print(my_string)