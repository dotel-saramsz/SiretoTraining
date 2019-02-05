import random
alphalist = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']


def encrypt(plaintext, key):
    mapencrypt = dict(zip(alphalist, [k for k in key]))
    ciphertext = ''
    for letter in plaintext:
        try:
            ciphertext += mapencrypt[letter.lower()]
        except KeyError:
            try:
                ciphertext += mapencrypt[letter.lower()].upper()
            except KeyError:
                ciphertext += letter
    return ciphertext


def decrypt(ciphertext, key):
    mapdecrypt = dict(zip([k for k in key], alphalist))
    plaintext = ''
    for letter in ciphertext:
        try:
            plaintext += mapdecrypt[letter.lower()]
        except KeyError:
            try:
                plaintext += mapdecrypt[letter.lower()].upper()
            except KeyError:
                plaintext += letter
    return plaintext


def main():
    cipherkey = random.sample(alphalist, 26)
    plaintext = "The quick brown fox jumped over the lazy dog"
    ciphertext = encrypt(plaintext, cipherkey)
    decipheredtext = decrypt(ciphertext, cipherkey)
    print('plaintext: {}'.format(plaintext))
    print('key: {}'.format(''.join(cipherkey)))
    print('ciphertext: {}'.format(ciphertext))
    print('decipheredtext: {}'.format(decipheredtext))


if __name__ == '__main__':
    main()