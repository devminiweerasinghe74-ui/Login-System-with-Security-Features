import string, hashlib

#hashed password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(input_password,stored_hash):
    return hash_password(input_password) == stored_hash

def password_strength_checker(input_password):

    pass_length = len(input_password)

    has_upper = any(c.isupper() for c in input_password)
    has_digits = any(c.isdigit() for c in input_password)
    has_lower = any(c.islower() for c in input_password)
    has_symbols = any(c in string.punctuation for c in input_password)

    #scoring
    score = 0

    #length scoring
    if pass_length>=10:
        score += 2
    elif pass_length>=6:
        score += 1

    #Character checking
    if has_upper:
        score += 1
    if has_digits:
        score += 1
    if has_lower:
        score += 1
    if has_symbols:
        score += 1

    #strength checking
    if score<=2:
        strength = "Weak"
    elif score<=4:
        strength = "Medium"
    else:
        strength = "Strong"

    #Suggestion
    suggestion = []
    if pass_length<6:
        suggestion.append("The characters should be more than 6.")
    if not has_upper:
        suggestion.append("Insert uppercases.")
    if not has_digits:
        suggestion.append("Insert numbers.")
    if not has_lower:
        suggestion.append("Insert lowercases.")
    if not has_symbols:
        suggestion.append("Insert symbols.")

    return strength,suggestion
# test
# test



