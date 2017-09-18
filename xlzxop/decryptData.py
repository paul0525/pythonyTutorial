from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES, PKCS1_OAEP

file_in = open("encrypted_data.bin", "rb")

secret_code = "Unguessable"
private_key = RSA.import_key(open("rsa_key.pem").read(), passphrase=secret_code)

enc_session_key, nonce, tag, ciphertext = \
    [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

print enc_session_key
print nonce
print tag
print ciphertext

# Decrypt the session key with the public RSA key
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)
print session_key

# Decrypt the data with the AES session key
# cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
# data = cipher.decrypt_and_verify(ciphertext, tag)