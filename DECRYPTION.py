#!/usr/bin/env python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

import binascii as ba
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from Crypto.Cipher import AES
from cryptography.hazmat.backends import default_backend
from Crypto.Hash import SHA256
from cryptography.hazmat.primitives.kdf.x963kdf import X963KDF


def hkdf_func(shared_secret):
    backend = default_backend()
    info = b'mb_security'
    hkdf = HKDF(algorithm=hashes.SHA256(),length=32, info=info, backend = backend, salt=None)
    derived_key=hkdf.derive(shared_secret)
    print('hkdf: {}' .format(ba.hexlify(derived_key)))
    return derived_key

def aes_decrypt(encd, derived_key, iv):
    #cipher = Cipher(algorithms.AES(derived_key), modes.CBC(iv), backend=default_backend())
    decryption = AES.new(derived_key, AES.MODE_CBC, iv)
    plain_text = decryption.decrypt(encd)

    #decryptor = cipher.decryptor()
    #decryption1 = decryptor.update(encd)
    return plain_text

pass_key = ba.unhexlify("12334343")
derived_key=hkdf_func(pass_key)
data = "c425be88f15f4d14c92303e504380aa9"
iv = X963KDF(algorithm=hashes.SHA256(), length=16, sharedinfo=b"mb_security", backend=default_backend()).derive(pass_key)

data2="016f75b94ccd687d96ec93ba190de4ea"
datahex=bytes.fromhex(data)
datahex2=bytes.fromhex(data2)
text=aes_decrypt(datahex,derived_key,iv)
text2=aes_decrypt(datahex2,derived_key,iv)
print("text-->",text)
print("\ntext2-->", text2)

print("\ntext-->", ba.b2a_hex(text))
print("\ntext2-->", ba.b2a_hex(text2))


shared_key=ba.unhexlify("12334343")

print("Shared_key-->",shared_key)
b= b'12334343'
print(b)
