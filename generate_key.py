from cryptography.fernet import Fernet
import json
from config import FILEPATH, KEYPATH

key = Fernet.generate_key()
cipher_suite = Fernet(key)
print(key)

if __name__ == "__main__":

    with open('source.json', 'r') as f:
        test_data = json.load(f)


    json_bytes = json.dumps(test_data).encode('utf-8')
    encrypted_data = cipher_suite.encrypt(json_bytes)

    with open(FILEPATH, 'wb') as file:
        file.write(encrypted_data)

    with open(KEYPATH, 'wb') as file:
        file.write(key)

    with open(FILEPATH, 'rb') as file:
        encrypted_data = file.read()

    with open(KEYPATH, 'r') as file:
        cipher_key =  file.read()

    json_bytes = json.dumps(test_data).encode('utf-8')
    encrypted_data = Fernet(cipher_key).encrypt(json_bytes)

    decrypted_bytes = Fernet(cipher_key).decrypt(encrypted_data)
    decrypted_data = json.loads(decrypted_bytes.decode('utf-8'))

    print(encrypted_data)
    print(decrypted_data)

