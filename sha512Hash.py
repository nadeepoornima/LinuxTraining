import hashlib
import os

salt = os.urandom(32) 
password = input("Enter Your password :")

hash = hashlib.sha512( salt + password.encode('utf-8') ).hexdigest()
print(hash)
