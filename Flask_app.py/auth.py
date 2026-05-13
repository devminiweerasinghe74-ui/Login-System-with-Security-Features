from password_utils import (
    password_strength_checker,
    hash_password,
    verify_password
)

from database import connect_db

import re

# test
# test
# =========================
# EMAIL VALIDATION
# =========================
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)


# =========================
# REGISTER USER
# =========================
def register_user(user_name, password):

    user_name = user_name.strip()
    password = password.strip()

    # empty validation
    if not user_name or not password:
        return "Username and password cannot be empty!"

    # email validation
    if not is_valid_email(user_name):
        return "Invalid email format!"

    # password strength checking
    strength, suggestions = password_strength_checker(password)

    if strength == "Weak":
        return "Weak password! Suggestions: " + ", ".join(suggestions)

    # hash password
    hashed = hash_password(password)

    # database connection
    conn = connect_db()
    cursor = conn.cursor()

    try:
        # insert user
        cursor.execute(
            "INSERT INTO users(email, password) VALUES(?, ?)",
            (user_name, hashed)
        )

        conn.commit()

    except:
        conn.close()
        return "User already exists!"

    conn.close()

    return "Registration successful!"


# =========================
# LOGIN USER
# =========================
def login_user(user_name, password):

    user_name = user_name.strip()
    password = password.strip()

    # empty validation
    if not user_name or not password:
        return False, "Username and password cannot be empty!"

    conn = connect_db()
    cursor = conn.cursor()

    # find user
    cursor.execute(
        "SELECT password, locked FROM users WHERE email=?",
        (user_name,)
    )

    user = cursor.fetchone()

    # user not found
    if not user:
        conn.close()
        return False, "User not found!"

    stored_hash, locked = user

    # locked account
    if locked:
        conn.close()
        return False, "Account is locked!"

    # verify password
    if verify_password(password, stored_hash):
        conn.close()
        return True, "Login successful!"

    conn.close()

    return False, "Invalid username or password!"