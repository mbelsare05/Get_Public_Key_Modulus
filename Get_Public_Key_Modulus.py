import Crypto.PublicKey.RSA
import M2Crypto
import sys

x509 = M2Crypto.X509.load_cert(sys.argv[1],0)
publickey = x509.get_pubkey()
key = Crypto.PublicKey.RSA.importKey(publickey.as_der())

modulus = key.n
public_exponent = key.e

f =  open(sys.argv[2],'wb')
f.write(format(modulus,'02X'))
f.close()
#print modulus in hex
print format(modulus,'02X')
print 

print 
print hex(public_exponent)
