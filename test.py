
'''

from cryptography.fernet import Fernet

message='Hej på dig ?\n'
key = Fernet.generate_key()
#fernet object
fernet = Fernet(key=key)

enc_bytes=fernet.encrypt(message.encode())
print('The origingal message is :\n',message)
print('The encrypted massage is ;±n', enc_bytes)

print("Decrypted message is ... \n", fernet.decrypt(enc_bytes).decode())

'''

import rsa

public_key,private_key =rsa.newkeys(512)
message=input('Hej paa dig ?\n')
enc_bytes=rsa.encrypt(message.encode(),public_key)

print('The origingal message is :\n',message)
print('The encrypted massage is ;\n', enc_bytes)
print("private key is :{}".format(private_key))

print('\n')
print(type(private_key))
prv_key=input("Submit private key")

decode_msg=rsa.decrypt(enc_bytes,prv_key)
print('Det decodate meddelandet är : {}'.format(decode_msg))