from Crypto.Cipher import AES
import sys
keystring = '00000000000000000000000000000000'
iostoken = sys.argv[1]
key = bytes.fromhex(keystring)
cipher = AES.new(key, AES.MODE_ECB)
token = cipher.decrypt(bytes.fromhex(iostoken[:64]))
print(token)
