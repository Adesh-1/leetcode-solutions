# 557. Reverse Words in a String III
# in python
  # ➡️ 1st method
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(map(lambda x: x[::-1], s.split()))

  # ➡️ 2nd method
class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.strip().split()
        ls=[]
        for i in l:
                ls.append(i[::-1])
        return " ".join(ls)
