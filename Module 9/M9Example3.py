#Iana Vasileva  CIS160 B65   M9Ex3    10/24/26
#Write a function that accepts the string and returns all lower case when the
#original string is all upper or mixed. If the original string is all lower then make the string all
#upper case. The function should return the new string.


#Define function
def change_case(original_string):
    if original_string.islower():
        new_string=original_string.upper()
    else:
        new_string=original_string.lower()
    return new_string

#Input
original_string=str(input("Enter a string:"))

#call the function
new_string=change_case(original_string)

#Display original and new strings
print("Original String:",original_string)
print("New String:",new_string)
