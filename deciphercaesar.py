import caesarcipher

orgtext = "The quick brown fox jumped over the lazy dog 12345"
ciphertext = caesarcipher.encrypt(orgtext, key=19)

#bruteforcing to decipher

for key in range(26):
    decipheredtext = caesarcipher.decrypt(ciphertext, key)
    if decipheredtext == orgtext:
        print('Deciphered!\nkey={}\nplaintext={}'.format(key, decipheredtext))
