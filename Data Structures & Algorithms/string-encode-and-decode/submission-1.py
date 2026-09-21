class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""

        for word in strs:
            encoded_string += str(len(word)) + "#" + word

        return encoded_string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])

            result.append(s[j + 1:j + 1 + length])

            i = j + 1 + length

        return result
