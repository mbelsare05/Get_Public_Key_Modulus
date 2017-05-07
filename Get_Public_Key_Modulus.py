import Crypto.PublicKey.RSA
import M2Crypto
import sys

help_text = """Usage : Get_Public_Key_Modulus.py In_Public.cer Out_Modulus.pem

"""

def print_help():
	print help_text


def extractModulus(Certificate):
	x509 = M2Crypto.X509.load_cert(Certificate,0)
	publickey = x509.get_pubkey()
	key = Crypto.PublicKey.RSA.importKey(publickey.as_der())
	modulus = key.n
	public_exponent = key.e
	return modulus


def writeBinFile(filename, data):
	f =  open(filename,'wb')
	f.write(format(data,'02X'))
	f.close()


def printHex(data):
	#print data in hex, 02 for byte and X for uppercase Hex alphabets
	print format(data,'02X')
	print 
	

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print_help()
		sys.exit(1)
	
	mod = extractModulus(sys.argv[1])
	printHex(mod)
	sys.exit(0)




