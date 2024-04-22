from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

# Зчитування приватного ключа з файлу
with open("private_key.pem", "rb") as priv_key_file:
    private_key = serialization.load_pem_private_key(
        priv_key_file.read(),
        password=None,
        backend=default_backend()
    )

# Зчитування публічного ключа з файлу (це для демонстрації, можна використати отриманий публічний ключ)
with open("public_key.pem", "rb") as pub_key_file:
    public_key = serialization.load_pem_public_key(
        pub_key_file.read(),
        backend=default_backend()
    )

# Повідомлення, яке потрібно підписати
message = b"Dotsenko#30.10.2002#2:50#85"

# Підпис повідомлення приватним ключем
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Перевірка підпису за допомогою публічного ключа
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Підпис перевірено успішно.")
except:
    print("Помилка перевірки підпису.")
