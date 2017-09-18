#coding=utf-8

from Cryptodome.PublicKey import RSA

secret_code = "Unguessable"
key = RSA.generate(2048)
encrypted_key = key.exportKey(passphrase=secret_code, pkcs=8,
                              protection="scryptAndAES128-CBC")

file_out = open("rsa_key.pem", "wb")
file_out.write(encrypted_key)

publickey = key.publickey().exportKey()
print publickey

file_out_public = open("receiver.pem","wb")
file_out_public.write( key.publickey().exportKey() )

