# 1859. Sorting the Sentence
# in python
class Solution:
    def sortSentence(self, s: str) -> str:
        l = s.split()
        nl = [""] * len(l)
        for word in l:
            ind = int(word[-1]) - 1
            nl[ind] = word[:-1]  # word[:-1] --> word[len(word)-1]
        return " ".join(nl)
