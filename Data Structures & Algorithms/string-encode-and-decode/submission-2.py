class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word
        print("Encoded: ", s)
        return s
    def decode(self, s: str) -> List[str]:   
        st = []
        i = 0
        length = len(s)
        while (i < length):
            j = i
            while (s[j] != "#"):
                j += 1
            skip = int(s[i:j])
            j += 1

            st.append(s[j: j + skip])

            i = j + skip
        return st
