import hashlib

def sha3_256_hash(data):
    hash_object = hashlib.sha3_256(data.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig

with open("input.txt", "r", encoding="utf-8") as file:
    message = file.read()

hashed_message = sha3_256_hash(message)

with open("encoded.txt", "w", encoding="utf-8") as file:
    file.write(hashed_message)

print("Хешоване повідомлення збережено у файлі encoded.txt")
