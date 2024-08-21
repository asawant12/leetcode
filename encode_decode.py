# https://leetcode.com/problems/encode-and-decode-strings/description/

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_strs = ""

        for st in strs:
            encoded_strs += str(len(st))+"#"+st
            
        return encoded_strs

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_strs = []
        indx = 0
        while indx < len(s):
            token_len=""
            while s[indx] != "#":
                token_len += s[indx]
                indx += 1
            indx += 1
            end_ptr = indx + int(token_len)
            decoded_strs.append(s[indx:end_ptr])
            indx = end_ptr
        return decoded_strs

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
