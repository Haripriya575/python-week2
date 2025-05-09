import re

def is_valid_email(email):

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

# Test cases
print(is_valid_email("user@domain.com"))   
print(is_valid_email("user@domain"))       
print(is_valid_email("userdomain.com"))    
print(is_valid_email("user@.com"))         
print(is_valid_email("user.name@domain.com"))  
