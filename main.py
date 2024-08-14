import re

def password_strength(password):
    # Criteria
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[@$!%*?&#]', password))

    # Initial strength
    strength = 0
    feedback = []

    # Check length
    if length >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letter
    if has_upper:
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letter
    if has_lower:
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for digit
    if has_digit:
        strength += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # Check for special character
    if has_special:
        strength += 1
    else:
        feedback.append("Password should contain at least one special character (@$!%*?&#).")

    # Determine overall strength
    if strength == 5:
        feedback.insert(0, "Password strength: Very strong")
    elif strength >= 4:
        feedback.insert(0, "Password strength: Strong")
    elif strength >= 3:
        feedback.insert(0, "Password strength: Moderate")
    else:
        feedback.insert(0, "Password strength: Weak")

    return "\n".join(feedback)

# Example usage
password = input("Enter a password to assess its strength: ")
print(password_strength(password))
