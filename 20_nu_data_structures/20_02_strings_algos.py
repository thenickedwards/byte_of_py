# STRINGS
# strings are immutable (unlike JavaScript)
# variables are mutable :D
# both double quotes "" and single quotes '' valid
# backticks not allowed ``
# """triple double quotes for multiline comments""" '''triple single quotes also work'''

message = "Hello"
# message[0] = "J"      # this will error

unstripped_str = " hello "
print(unstripped_str)    # whitespace included
clean_str = unstripped_str.strip()
print(clean_str)        # hello