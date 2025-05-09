# Initial list of users
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

# Create
def add_user(user_id, name, email):
    for user in users:
        if user["id"] == user_id:
            print("User ID already exists.")
            return
    users.append({"id": user_id, "name": name, "email": email})
    print("User added successfully.")

# Read
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return "User not found."

# Update
def update_user(user_id, name=None, email=None):
    for user in users:
        if user["id"] == user_id:
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            print("User updated successfully.")
            return
    print("User not found.")

# Delete
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            print("User deleted successfully.")
            return
    print("User not found.")

# Display all users
def display_users():
    print("\nCurrent Users:")
    for user in users:
        print(user)

# Demo execution
if __name__ == "__main__":
    display_users()

    print("\n--- Adding User ---")
    add_user(3, "Charlie", "charlie@example.com")
    display_users()

    print("\n--- Reading User ID 2 ---")
    print(get_user(2))

    print("\n--- Updating User ID 1 ---")
    update_user(1, name="Alice Smith")
    display_users()

    print("\n--- Deleting User ID 2 ---")
    delete_user(2)
    display_users()
