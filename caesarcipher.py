alphalist = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']
tonum = dict(zip(alphalist, range(0, 26)))
toletter = dict(zip(range(0, 26), alphalist))
plaintext = "The quick brown fox jumped over the lazy dog 12345"


#Encryption
def encrypt(plaintext, key=4):
    ciphertext = ''
    for i, letter in enumerate(plaintext):
        try:
            ciphertext += toletter[(tonum[plaintext[i].lower()] + key) % 26]
        except KeyError:
            ciphertext += plaintext[i]
    return ciphertext


#Decryption
def decrypt(ciphertext, key=4):
    decipheredtext = ''
    for i, letter in enumerate(ciphertext):
        try:
            decipheredtext += toletter[(tonum[ciphertext[i].lower()]-key) % 26]
        except:
            decipheredtext += ciphertext[i]
    return decipheredtext

def main():
    print('plaintext: {}'.format(plaintext))
    print('ciphertext: {}'.format(encrypt(plaintext)))

    print('decipheredtext: {}'.format(decrypt(encrypt(plaintext))))

if __name__ == '__main__':
    main()
