import re

def evaluate_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if contains_common_pattern(password):
        score -= 1

    strength = strength_score(score)

    print(f"Strength - {strength}")
    print(f"Score - {score}")

def contains_common_pattern(password):
    weak_patterns = [
        "password",
        "1234",
        "qwerty",
        "admin",
        "letmein"
    ]

    lower = password.lower()

    for pattern in weak_patterns:
        if pattern in lower:
            return True
    return False

def strength_score(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"

def main():
    password = input("Enter a password - ")
    evaluate_password(password)

if __name__ == "__main__":
    main()
