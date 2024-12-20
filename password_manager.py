from cryptography.fernet import Fernet

def write_key():
    """Generate and save a new Fernet key."""
    key = Fernet.generate_key()  # Generate a valid Fernet key
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """Load the Fernet key from the file."""
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Ensure the key exists before proceeding
try:
    key = load_key()
except FileNotFoundError:
    write_key()
    key = load_key()

# Validate and initialize Fernet with the key
if len(key) != 44:  # Base64-encoded 32-byte keys are 44 characters long
    raise ValueError("The loaded key is invalid. Please delete 'key.key' and restart the program.")

fer = Fernet(key)

def view():
    """View saved account passwords."""
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                line = line.strip()  # Remove trailing whitespace and newlines
                if "|" not in line:  # Check for valid format
                    print(f"Malformed line ignored: {line}")
                    continue
                try:
                    user, encrypted_passw = line.split("|")
                    decrypted_passw = fer.decrypt(encrypted_passw.encode()).decode()
                    print(f"User: {user}, Password: {decrypted_passw}")
                except Exception as e:
                    print(f"Error decrypting line: {line}. Error: {e}")
    except FileNotFoundError:
        print("No saved passwords found.")


def add():
    """Add a new account password."""
    name = input("Account Name: ")
    pwd = input("Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    with open('passwords.txt', 'a') as f:
        f.write(f"{name}|{encrypted_pwd}\n")
    print("Password saved successfully.")

while True:
    mode = input("Would you like to add a new password or view existing ones (view/add), or press q to quit: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")

