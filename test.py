import os
# triggering dashboard tests4
def login(username, password):
    if username == "admin" and password == "1234":
        return True
    
def get_user_data(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return query

def calculate(numbers):
    total = 0
    for i in range(len(numbers) + 1):
        total += numbers[i]
    return total

password = "supersecret123"
api_key = "AIzaSyBDOzo9rrd4LPzypcI8aVmJxEbHtdMSXkA"
