import string

password = input("Enter a password to test: ")

score = 0
print("\n--- HACKER ANALYSIS ---")

if len(password) >= 8:
    print("[+] Length OK (8+ chars)")
    score += 1
else:
    print("[-] Too short! Hackers crack this in seconds")

if any(c in string.ascii_lowercase for c in password) and any(c in string.ascii_uppercase for c in password):
    print("[+] Has Upper + Lower case")
    score += 1
else:
    print("[-] No mix of upper/lower")

if any(c in string.digits for c in password):
    print("[+] Has numbers")
    score += 1
else:
    print("[-] No numbers - easy to guess")

if any(c in string.punctuation for c in password):
    print("[+] Has symbols like !@#")
    score += 1
else:
    print("[-] No symbols")

print("\nSTRENGTH:", score, "/4")
if score == 4:
    print("Result: STRONG - Hard to hack!")
elif score >= 2:
    print("Result: MEDIUM - A hacker could crack it")
else:
    print("Result: WEAK - Hackable in < 1 minute!")
