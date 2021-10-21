from cryptography import fernet
from cryptography.fernet import Fernet

#This class is used to encrypt/decrypt the user password
class Encryption ():

    def gen_key():
        #check if key already exist
        #if not (self.check_key()):
        key = Fernet.generate_key()
        print(key)
        with open ("key_store","wb") as k:
            k.write(key)

# This method check if the exist 
    def check_key(self):
        try:
            if(open("key_store", "rb").read()):
                return True
        except:
            return False 
#This method return the key
    def load_key (self):
        return (open("key_store","rb").read())

#This method encrypt the message
    def encrypt(self,message):
        key = self.load_key()
        encoded_message= message.encode()
        f = Fernet(key)
        enc_message = f.encrypt(encoded_message)
        return enc_message

#This method decrypt the message   
    def decrypt(self,message):
        key = self.load_key()
        f=Fernet(key)
        dec_message = f.decrypt(message)
        return dec_message