class Solution:
    def encode(self, strs: list[str]) -> str:
        """
        Encodes a list of strings into a single string using the Length-Prefix method.
        Example: ["a", "b"] -> "1#a1#b"
        """
        encoded_string = []
        for s in strs:
            # Append the length of the string, a delimiter (#), and the string itself.
            encoded_string.append(str(len(s)) + "#" + s)
        
        return "".join(encoded_string)

    def decode(self, s: str) -> list[str]:
        """
        Decodes a single string back to a list of strings.
        """
        decoded_list = []
        i = 0
        while i < len(s):
            # 1. Find the length prefix
            j = i
            while s[j] != '#':
                j += 1
            
            # The number is the substring from i up to j
            length = int(s[i:j])
            
            # 2. Extract the string
            # Start of the string is after the delimiter (j + 1)
            # End of the string is (j + 1 + length)
            start_index = j + 1
            end_index = start_index + length
            
            decoded_list.append(s[start_index:end_index])
            
            # 3. Move the pointer (i) to the start of the next potential prefix
            i = end_index
            
        return decoded_list