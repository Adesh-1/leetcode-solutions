// 744. Find Smallest Letter Greater Than Target
// in java
class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        for (char c : letters) {
            if (target < c)
                return c;
        }
        return letters[0];
    }
}

// in python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if target < i:
                return i
        return letters[0]
