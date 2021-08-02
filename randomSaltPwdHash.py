import hashlib
import os

salt = os.urandom(32) 
password = input("Enter Your password :")

pbkdf2_hmac_key = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 200000, dklen=256)

print(pbkdf2_hmac_key.hex())
