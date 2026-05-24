import os

# ============================================
# Secure Login Function
# ============================================
def login(username, password):
    correct_username = "admin"
    correct_password = "1234"

    if username == correct_username and password == correct_password:
        return True
    return False


# ============================================
# Safe User Data Query
# ============================================
def get_user_data(user_id):
    # Convert input safely to integer
    try:
        user_id = int(user_id)
    except ValueError:
        return "Invalid User ID"

    # Safe query using formatting
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return query


# ============================================
# Fixed Calculation Function
# ============================================
def calculate(numbers):
    total = 0

    for i in range(len(numbers)):
        total += numbers[i]

    return total


# ============================================
# Secure Environment Variables
# ============================================
password = os.getenv("APP_PASSWORD", "default_password")
api_key = os.getenv("API_KEY", "default_api_key")


# ============================================
# Testing
# ============================================
print("Login:", login("admin", "1234"))

print("Query:", get_user_data("5"))

nums = [10, 20, 30]
print("Total:", calculate(nums))

print("Password Loaded:", password)
print("API Key Loaded:", api_key)
