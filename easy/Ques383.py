# 383. Ransom Note
# in python

# 1st method
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = Counter(ransomNote)
        d2 = Counter(magazine)
        for i in d1:
            if d1[i] > d2[i]:
                return False
        return True

# 2nd method
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not (Counter(ransomNote) - Counter(magazine))

# for more info. follow below given link
# https://chatgpt.com/share/690248c6-cc68-8001-860a-b5c6a57e4084

