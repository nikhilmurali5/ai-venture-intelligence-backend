from app.core.security import hash_password

password = "secret123"

hashed = hash_password(password)

print("Original:", password)
print("Hashed:", hashed)