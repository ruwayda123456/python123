import hashlib
import sys

someText = raw_input("Enter the string to be hashed:")

def hashSha1( some_string):
	output = hashlib.sha1(some_string)
	print('HASH-1= ' + output.hexdigest())
	

def hashSha256(some_string):
	output = hashlib.sha256(some_string)
	print('HASH-256= ' + output.hexdigest())
	

def hashSha512(some_string):
	output = hashlib.sha512(some_string)
	print('HASH-512= ' + output.hexdigest())
	


	

hashSha1(someText);
hashSha256(someText);
hashSha512(someText);