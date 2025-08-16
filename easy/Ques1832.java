// 1832. Check if the Sentence Is Pangram
// in java
class Solution {
    public boolean checkIfPangram(String sentence) {
        Set<Character> s = new HashSet<>();
        for(char c : sentence.toCharArray())
            s.add(c);
        return s.size() == 26;
    }
}

// in py
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
