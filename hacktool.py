import socket, base64, random, string, os

def check_pass():
    pwd = input("\nEnter password: ")
    score = 0
    if len(pwd) >= 8: score+=1
    if any(c.isupper() for c in pwd) and any(c.islower() for c in pwd): score+=1
    if any(c.isdigit() for c in pwd): score+=1
    if any(c in "!@#$%^&*" for c in pwd): score+=1
    print(f"STRENGTH: {score}/4 - {'STRONG!' if score==4 else 'WEAK!'}")

def scan():
    target = input("\nEnter site (google.com): ")
    print(f"Scanning {target}...")
    for p in [21,22,80,443]:
        s=socket.socket(); s.settimeout(1)
        if s.connect_ex((target,p))==0:
            print(f"[OPEN] Port {p}")
        s.close()

def secret():
    msg=input("\nSecret message: ")
    enc=base64.b64encode(msg.encode()).decode()
    print(f"Hidden: {enc}")

def gen():
    length=int(input("\nLength (12-24): "))
    chars=string.ascii_letters+string.digits+"!@#$"
    pwd="".join(random.choice(chars) for _ in range(length))
    print(f"\nPassword: {pwd}")

while True:
    print("\n--- MY HACKER TOOLKIT v1.0 ---")
    print("1. Password Checker")
    print("2. Port Scanner")
    print("3. Secret Encoder")
    print("4. WiFi Generator")
    print("5. Exit")
    c=input("Choose (1-5): ")
    if c=="1": check_pass()
    elif c=="2": scan()
    elif c=="3": secret()
    elif c=="4": gen()
    elif c=="5": break
