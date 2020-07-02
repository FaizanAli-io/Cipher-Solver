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

    def ADFGVX(self, hashkey=None):
        if hashkey:
            hashkey = list(hashkey)
        else:
            hashkey = [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]
            random.shuffle(hashkey)
        ciphertext = ''
        spacecode = ''.join([i for i in hashkey if i.isdecimal()][:3])
        self.data = self.data.replace(' ', spacecode)
        for i in self.data:
            ciphertext += 'adfgvx'[hashkey.index(i) // 6] + 'adfgvx'[hashkey.index(i) % 6]
        return ciphertext, ''.join(hashkey)

    def decode_ADFGVX(self, hashkey):
        coords, i = [], 0
        while i < len(self.data):
            x, y = 'adfgvx'.index(self.data[i]), 'adfgvx'.index(self.data[i+1])
            coords.append((x, y))
            i += 2
        hashkey2 = self.chunkify(list(hashkey), 6)
        plaintext = ''
        for coord in coords:
            plaintext += hashkey2[coord[0]][coord[1]]
        spacecode = ''.join([i for i in hashkey if i.isdecimal()][:3])
        plaintext = plaintext.replace(spacecode, ' ')
        return plaintext
