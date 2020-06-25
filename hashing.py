import math, random

class encode:
    def __init__(self, s):
        self.data = s

    @staticmethod
    def chunkify(s, n): return [s[b:b+n] for b in range(0, len(s), n)]

    def caesar(self, shift: int):
        key = [chr(i) for i in range(97, 123)]
        shifted = key[shift:] + key[:shift]
        ciphertext = ''
        for letter in self.data:
            ciphertext += shifted[key.index(letter)]
        return ciphertext

    def decode_caesar(self, shift: int):
        key = [chr(i) for i in range(97, 123)]
        shifted = key[shift:] + key[:shift]
        plaintext = ''
        for letter in self.data:
            plaintext += key[shifted.index(letter)]
        return plaintext

    def vigenere(self, key: str):
        ref = [chr(i) for i in range(97, 123)]
        grid = [ref[i:] + ref[:i] for i in range(26)]
        while len(key) < len(self.data):
            key += key
        if len(key) > len(self.data):
            key = key[:len(self.data)]
        ciphertext = ''
        for i, j in zip(self.data, key):
            i, j = ord(i)-97, ord(j)-97
            ciphertext += grid[i][j]
        return ciphertext

    def decode_vigenere(self, key: str):
        ref = [chr(i) for i in range(97, 123)]
        grid = [ref[i:] + ref[:i] for i in range(26)]
        while len(key) < len(self.data):
            key += key
        if len(key) > len(self.data):
            key = key[:len(self.data)]
        plaintext = ''
        for i, j in zip(key, self.data):
            i = ord(i)-97
            index = grid[i].index(j)
            plaintext += ref[index]
        return plaintext

    def matrix(self, rows: int):
        chunks = self.chunkify(self.data, rows)
        while len(chunks[-1]) != rows:
            chunks[-1] += '#'
        ciphertext = ''
        for i in range(rows):
            for chunk in chunks:
                ciphertext += chunk[i]
        return ciphertext

    def decode_matrix(self, rows: int):
        if len(self.data) % rows != 0:
            return "Invalid Matrix Key"
        columns = len(self.data)//rows
        chunks = self.chunkify(self.data, columns)
        plaintext = ''
        for i in range(columns):
            for chunk in chunks:
                plaintext += chunk[i]
        return plaintext.replace('#', '')

    def porta(self, key: str):
        ref = [chr(i) for i in range(97, 123)]
        grid = [ref[13:]+ref[:13]]
        for i in range(12):
            grid.append(grid[i][1:13] + [grid[i][0]] + [grid[i][-1]] + grid[i][13:-1])
        while len(key) < len(self.data):
            key += key
        if len(key) > len(self.data):
            key = key[:len(self.data)]
        ciphertext = ''
        for i, j in zip(self.data, key):
            i, j = ord(i)-97, (ord(j)-97)//2
            ciphertext += grid[j][i]
        return ciphertext
    
    def decode_porta(self, key: str):
        ref = [chr(i) for i in range(97, 123)]
        grid = [ref[13:]+ref[:13]]
        for i in range(12):
            grid.append(grid[i][1:13] + [grid[i][0]] + [grid[i][-1]] + grid[i][13:-1])
        while len(key) < len(self.data):
            key += key
        if len(key) > len(self.data):
            key = key[:len(self.data)]
        plaintext = ''
        for i, j in zip(self.data, key):
            i, j = ord(i)-97, (ord(j)-97)//2
            plaintext += grid[j][i]
        return plaintext

    def ADFGVX(self, word, hashkey=None):
        if hashkey:
            hashkey = list(hashkey)
        else:
            hashkey = [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]
            random.shuffle(hashkey)
        cipher = ''
        for i in self.data:
            cipher += 'adfgvx'[hashkey.index(i) // 6] + 'adfgvx'[hashkey.index(i) % 6]
        i = 0
        j = 0
        while len(cipher) % len(word) != 0:
            cipher += '#'
        myli = [[i.upper()] for i in word]
        while i < len(cipher):
            myli[j].append(cipher[i])
            i += 1
            j += 1
            if j >= len(myli): j = 0
        myli = sorted(myli, key=lambda x: x[0])
        [li.pop(0) for li in myli]
        return ''.join([''.join(row) for row in myli]), ''.join(hashkey)

    def decode_ADFGVX(self, hashkey, word):
        wordorig = word.upper()
        word = sorted(wordorig)
        myli = [[letter] for letter in word]
        chsize = len(self.data)//len(word)
        for i in range(len(myli)):
            myli[i].append(self.data[:chsize])
            self.data = self.data[chsize:]
        myli2 = []
        for letter in wordorig:
            for item in myli:
                if item[0] == letter:
                    myli2.append(item)
        
        myli2 = [i[-1] for i in myli2]
        cipher = ''
        for i in range(len(myli2[0])):
            for item in myli2:
                if item[i] != '#': cipher += item[i]
        coords = []
        i = 0
        while i < len(cipher):
            x, y = 'adfgvx'.index(cipher[i]), 'adfgvx'.index(cipher[i+1])
            coords.append((x, y))
            i += 2
        hashkey = self.chunkify(list(hashkey), 6)
        plaintext = ''
        for coord in coords:
            plaintext += hashkey[coord[0]][coord[1]]
        return plaintext

if __name__ == "__main__":
    print("hello world")