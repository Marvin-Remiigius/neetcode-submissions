class Solution:

    def encode(self, strs: List[str]) -> str:
        encrypted_string = ""

        for s in strs:
            encrypted_string += str(len(s)) + "#"

            for ch in s:
                encrypted_string += chr(ord(ch) + 3)

        return encrypted_string

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0

        while i < len(s):
            # Read the length
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # Move past '#'
            j += 1

            decrypted_string = ""
            for k in range(j, j + length):
                decrypted_string += chr(ord(s[k]) - 3)

            words.append(decrypted_string)

            # Move to the next encoded string
            i = j + length

        return words