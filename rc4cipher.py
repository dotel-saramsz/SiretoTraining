class RC4cipher:
    def __init__(self, inputkey):
        self.key = list(map(ord, inputkey))
        # KSA (Key Scheduling Algorithm)
        # initialize the state vector
        self.s = list(range(256))
        j = 0
        for i in range(256):
            j = (j + self.s[i] + self.key[i % len(self.key)]) % 256
            self.s[i], self.s[j] = self.s[j], self.s[i]
        self.i = 0
        self.j = 0
        self.keystream = []

    # PRGA (Pseudo Random Generation Algorithm)
    def generate_keystream(self):
        self.i = (self.i+1) % 256
        self.j = (self.j+self.s[self.i]) % 256
        self.s[self.i], self.s[self.j] = self.s[self.j], self.s[self.i]
        return self.s[(self.s[self.i]+self.s[self.j]) % 256]

    def encrypt(self, plaintext):
        ciphertext = ''
        for letter in plaintext:
            key = self.generate_keystream()
            self.keystream.append(key)
            xor = ord(letter)^key
            print(key)
            ciphertext += chr(xor)
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ''
        for i, letter in enumerate(ciphertext):
            key = self.keystream[i]
            plaintext += chr(ord(letter)^key)
        return plaintext

def main():
    # define input key to be of 16 bytes
    key = 'pwd12fgytrevbqu'
    rc4 = RC4cipher(key)
    plaintext = 'Abcdef GHijkl'
    ciphertext = rc4.encrypt(plaintext)
    decipheredtext = rc4.decrypt(ciphertext)
    print('plaintext: {}'.format(plaintext))
    print('ciphertext: {}'.format(ciphertext))
    print('decipheredtext: {}'.format(decipheredtext))


if __name__ == '__main__':
    main()



