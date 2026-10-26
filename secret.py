import base64

msg = input("Enter secret message: ")
encoded = base64.b64encode(msg.encode()).decode()
print(f"\nEncoded (hidden): {encoded}")

decoded = base64.b64decode(encoded).decode()
print(f"Decoded (original): {decoded}")
