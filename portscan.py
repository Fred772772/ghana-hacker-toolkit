import socket

target = input("Enter website to scan (e.g. google.com): ")
print(f"\nScanning {target}...\n")

for port in [21, 22, 80, 443, 8080]:
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[OPEN] Port {port} is open!")
    else:
        print(f"[CLOSED] Port {port} closed")
    s.close()

print("\nScan Done!")
import socket

target = input("Enter website to scan (e.g. google.com): ")
print(f"\nScanning {target}...\n")

for port in [21, 22, 80, 443, 8080]:
    s = socket.socket()
    s.settimeout(1)
    try:
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port} is open!")
        else:
            print(f"[CLOSED] Port {port} closed")
    except:
        print(f"[ERROR] Could not connect to {target}")
        break
    s.close()

print("\nScan Done!")
