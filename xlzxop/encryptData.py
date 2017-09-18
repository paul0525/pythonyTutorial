#coding=utf-8
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_OAEP

file_out = open("encrypted_data.bin", "wb")

recipient_key = RSA.import_key(open("receiver.pem").read())
session_key = "abcd"

# Encrypt the session key with the public RSA key
cipher_rsa = PKCS1_OAEP.new(recipient_key)
file_out.write(cipher_rsa.encrypt(session_key))

# Encrypt the data with the AES session key
#cipher_aes = AES.new(session_key, AES.MODE_EAX)
#ciphertext, tag = cipher_aes.encrypt_and_digest("hello python ")
#[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]