import string

def evaluate_password(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters, preferably 12.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add a number.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add a special character.")

    if score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    print("\nPassword Strength:", strength)

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print("-", item)
    else:
        print("Your password meets all the checks!")

password = input("Enter a password to evaluate: ")
evaluate_password(password)
