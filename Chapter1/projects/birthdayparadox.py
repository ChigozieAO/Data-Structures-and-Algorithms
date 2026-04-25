import random

def generate_birthdays(n):
    return [random.randint(1, 365) for _ in range(n)]

def has_duplicate(birthdays):
    seen = set()
    for day in birthdays:
        if day in seen:
            return True
        seen.add(day)
    return False

def run_experiment(n):
    birthdays = generate_birthdays(n)
    return has_duplicate(birthdays)

def estimate_probability(n, trials=1000):
    matches = 0
    for _ in range(trials):
        if run_experiment(n):
            matches += 1
    return matches / trials

def test_birthday_paradox():
    for n in range(5, 101, 5):
        prob = estimate_probability(n)
        print(f"n = {n}, probability ≈ {prob:.3f}")

test_birthday_paradox()