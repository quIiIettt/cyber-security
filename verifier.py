import hashlib

def sha3_224_hash(data):
    hash_object = hashlib.sha3_224(data.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig

def verify_digest(message, stored_hash):
    hashed_message = sha3_224_hash(message)
    if hashed_message == stored_hash:
        return f"Дайджест співпадає зі збереженим. Повідомлення: {message}"
    else:
        return "Увага! Дайджест не співпадає зі збереженим."

# Зчитування збереженого хешу з файлу output.txt
with open("encoded.txt", "r", encoding="utf-8") as file:
    stored_hashes = file.readlines()
    stored_hashes = [hash.strip() for hash in stored_hashes]

# Перевірка кожного повідомлення з файлу message.txt
with open("message.txt", "r", encoding="utf-8") as file:
    messages = file.readlines()
    for i, message in enumerate(messages):
        message = message.strip()
        if i < len(stored_hashes):
            result = verify_digest(message, stored_hashes[i])
            print(f"Результат для повідомлення {i+1}: {result}")
        else:
            print(f"Увага! Немає збереженого хешу для повідомлення {i+1}.")
