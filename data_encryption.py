import pyAesCrypt
from Crypto.Cipher import AES
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
from arc4 import ARC4
from itertools import *

from cryptography.fernet import Fernet

'''
def xor_data_encode(input_data,password):	-> return cipher_data
def xor_data_decode(cipher_data,password):	-> return plain_data
def rc4_data_encrypt(plain_data, password):	-> return cipher_data
def rc4_data_decrypt(cipher_data, password):	-> return plain_data
def aes_data_encrypt(plain_data,aes_key):	-> return cipher_data
def aes_data_decrypt(cipher_data,aes_key):	-> return plain_data
'''
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

#Generates a key and save it into a file
def write_key():
	key = Fernet.generate_key()
	with open("key.key", "wb") as key_file:
		key_file.write(key)

#Loads the key from the current directory named `key.key`
def load_key():
	return open("key.key", "rb").read()


#Given a filename (str) and key (bytes), it encrypt the file and write it
def encrypt_file_fernet(filename, key):
	f = Fernet(key)
	with open(filename, "rb") as file:
		# read all file data
		file_data = file.read()
	encrypted_data = f.encrypt(file_data)
	with open("1.enc", "wb") as file:
		file.write(encrypted_data)

#Given a filename (str) and key (bytes), it decrypts the file and write it
def decrypt_file_fernet(filename, key):
	f = Fernet(key)
	with open(filename, "rb") as file:
		# read the encrypted data
		encrypted_data = file.read()
	# decrypt data
	decrypted_data = f.decrypt(encrypted_data)
	# write the original file
	with open("decrpt.xlsx", "wb") as file:
		file.write(decrypted_data)


#Write the data to file
def write_to_file(input_data,file_name):
	f = open(file_name, 'wb')
	f.write(input_data)
	f.close()
##
def xor_file_encode(input_file_name,output_file_name,password):
	plain_data=open(input_file_name).read()
	cipher_data = xor_data_encode(plain_data,password)
	open(output_file_name, 'w').write(''.join(cipher_data))
	return output_file_name

##
def xor_file_decode(encoded_file_name,output_file_name,password):
	cipher_data=open(encoded_file_name).read()
	plain_data = xor_data_decode(cipher_data,password)
	open(output_file_name, 'w').write(''.join(plain_data))
	return output_file_name


##Decode Data - XOR
def xor_data_encode(input_data,password):
	cipher_data = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(input_data, cycle(password)))
	return cipher_data

##Decode Data - XOR
def xor_data_decode(cipher_data,password):
	plain_data = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(cipher_data, cycle(password)))
	return plain_data


##Encrypt Data - RC4
def rc4_data_encrypt(plain_data, password):
	arc4 = ARC4(password)
	cipher_data = arc4.encrypt(plain_data)
	return cipher_data

##Decrypt Data - RC4
def rc4_data_decrypt(cipher_data, password):
	arc4 = ARC4(password)
	plain_data=arc4.decrypt(cipher_data)
	return plain_data

#Encrypt Data - AES
def aes_data_encrypt(plain_data, password):
	private_key = hashlib.sha256(password.encode("utf-8")).digest()
	plain_data = pad(plain_data)
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(private_key, AES.MODE_CBC, iv)
	cipher_data = base64.b64encode(iv + cipher.encrypt(plain_data))
	return cipher_data
 
#Decrypt Data - AES
def aes_data_decrypt(cipher_data, password):
	private_key = hashlib.sha256(password.encode("utf-8")).digest()
	cipher_data = base64.b64decode(cipher_data)
	iv = cipher_data[:16]
	cipher = AES.new(private_key, AES.MODE_CBC, iv)
	plain_data= unpad(cipher.decrypt(cipher_data[16:]))
	return plain_data


write_key()
key = load_key()
encrypt_file_fernet('Book1.xlsx',key);
decrypt_file_fernet('1.enc',key);


output_file=xor_file_encode('i.txt','123_enc','hello')
output_file=xor_file_decode('File_Enc','card.txt','hello')
#output_file=xor_file_encode('Output.xlsx','output_file','hello')

cipher_data=aes_data_encrypt('hello','852')
print(cipher_data)
plain_data=aes_data_decrypt(cipher_data,'852')
print(plain_data)
cipher_data=rc4_data_encrypt('hello','852')
print(cipher_data)
plain_data=rc4_data_decrypt(cipher_data,'852')
print(plain_data)
cipher_data=xor_data_encode('hello','852')
print(cipher_data)
plain_data=xor_data_decode(cipher_data,'852')
print(plain_data)
