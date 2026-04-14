# 824. Goat Latin
# in python
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        words = sentence.split()

        result = []

        for i, word in enumerate(words):
            if word[0] in vowels:
                new_word = word + "ma"
            else:
                new_word = word[1:] + word[0] + "ma"

            # add 'a' based on position
            new_word += "a" * (i + 1)

            result.append(new_word)

        return " ".join(result)

# in java
class Solution {
    public String toGoatLatin(String sentence) {
        String vowels = "aeiouAEIOU";
        String[] words = sentence.split(" ");
        
        StringBuilder result = new StringBuilder();
        
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            StringBuilder temp = new StringBuilder();
            
            # // Check if first letter is vowel
            if (vowels.indexOf(word.charAt(0)) != -1) {
                temp.append(word);
            } else {
                temp.append(word.substring(1));
                temp.append(word.charAt(0));
            }
            
            # // Add "ma"
            temp.append("ma");
            
            # // Add 'a' based on index
            for (int j = 0; j <= i; j++) {
                temp.append('a');
            }
            
            result.append(temp);
            
            # // Add space except last word
            if (i != words.length - 1) {
                result.append(" ");
            }
        }
        
        return result.toString();
    }
}
