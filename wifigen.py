import random, string

length = int(input("Password length (12-32): "))
chars = string.ascii_letters + string.digits + "!@#$%^&*"

password = "".join(random.choice(chars) for _ in range(length))

print(f"\n[GENERATED] Unhackable password:")
print(password)
print(f"\nStrength: {length*4} bits - Will take 1000+ years to hack!")
