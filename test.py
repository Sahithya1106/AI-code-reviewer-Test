import os
import bcrypt
import sqlite3
from typing import List

# ====================================================
# AUTHENTICATION - No hardcoded credentials
# ====================================================
def login(username: str, password: str) -> bool:
    # Passwords should be hashed and checked securely
    stored_hashed_password = os.getenv("ADMIN_PASSWORD_HASH", "")
    
    if not stored_hashed_password:
        return False
    
    # Compare using bcrypt - secure password checking
    is_valid = bcrypt.checkpw(
        password.encode("utf-8"),
        stored_hashed_password.encode("utf-8")
    )
    return is_valid

# ====================================================
# DATABASE - No SQL injection
# ====================================================
def get_user_data(user_id: int) -> list:
    conn = sqlite3.connect("mydb.db")
    cursor = conn.cursor()
    
    # Parameterized query - safe from SQL injection
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    result = cursor.fetchall()
    conn.close()
    return result

# ====================================================
# CALCULATION - No off-by-one error
# ====================================================
def calculate(numbers: List[int]) -> int:
    if not numbers:
        return 0
    # Clean way to sum a list
    return sum(numbers)

# ====================================================
# CREDENTIALS - Loaded from environment variables
# ====================================================
password = os.getenv("APP_PASSWORD", "")
api_key  = os.getenv("GEMINI_API_KEY", "")

if not password or not api_key:
    print("⚠️ Warning: Missing environment variables APP_PASSWORD or GEMINI_API_KEY")
