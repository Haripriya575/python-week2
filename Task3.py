import hashlib


users = {}


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register(username, password):
    if username in users:
        return "Error: Username already exists."
    hashed = hash_password(password)
    users[username] = hashed
    return "Created new user"


def login(username, password):
    hashed = hash_password(password)
    if username in users and users[username] == hashed:
        return "Login Successful"
    return "Login Failed"


print(register("john", "mypassword"))  
print(login("john", "mypassword"))     
print(login("john", "wrongpass"))      
print(register("john", "anotherpass")) 
