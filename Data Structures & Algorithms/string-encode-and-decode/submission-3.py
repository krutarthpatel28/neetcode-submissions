class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_string = ""
        for s in strs:
            # Format: <length of string>#<string itself>
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        decoded_strings = []
        i = 0
        
        while i < len(s):
            # Find the delimiter '#' to extract the length of the next string
            j = i
            while s[j] != "#":
                j += 1
            
            # Extract the length as an integer
            length = int(s[i:j])
            
            # The actual string starts right after '#' and spans 'length' characters
            word = s[j + 1 : j + 1 + length]
            decoded_strings.append(word)
            
            # Move the pointer to the start of the next encoded string
            i = j + 1 + length
            
        return decoded_strings