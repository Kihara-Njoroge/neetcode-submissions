class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result = []
        i= 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            # Length of the next string
            length = int(s[i:j])

            # Extract the string
            word = s[j +1  : j + 1 + length]
            result.append(word)

            # Move to the next encoded string
            i = j + 1 + length

        return result
