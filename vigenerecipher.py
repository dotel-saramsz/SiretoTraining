alphalist = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']
tonum = dict(zip(alphalist, range(0, 26)))
toalpha = dict(zip(range(0, 26), alphalist))


def encrypt(plaintext, key):
    ciphertext = ''
    cipherkey = ''
    plaintext = ''.join(plaintext.lower().split())
    for i in range(len(plaintext)):
        cipherkey += key[i % len(key)]
        ciphertext += toalpha[(tonum[plaintext[i]] + tonum[cipherkey[i]]) % 26]
    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ''
    cipherkey = ''
    for i in range(len(ciphertext)):
        cipherkey += key[i % len(key)]
        plaintext += toalpha[(tonum[ciphertext[i]] - tonum[cipherkey[i]]) % 26]
    return plaintext


def main():
    plaintext = 'The quick brown fox jumped over the lazy dog'
    cipherkey = 'helloworld'
    ciphertext = encrypt(plaintext, cipherkey)
    decipheredtext = decrypt(ciphertext, cipherkey)
    print('plaintext: {}'.format(plaintext))
    print('cipherkey: {}'.format(cipherkey))
    print('ciphertext: {}'.format(ciphertext))
    print('decipheredtext: {}'.format(decipheredtext))

if __name__ == '__main__':
    main()