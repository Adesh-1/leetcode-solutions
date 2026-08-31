# 3582. Generate Tag for Video Caption
# in python
class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()

        if not words:
            return "#"

        tag = "#" + words[0].lower()
        tag += "".join(word.capitalize() for word in words[1:])

        return tag[:100]

# in java
class Solution {
    public String generateTag(String caption) {
        if (caption.trim().isEmpty())
            return "#";

        String[] words = caption.trim().split("\\s+");

        StringBuilder tag = new StringBuilder("#");
        tag.append(words[0].toLowerCase());

        for (int i = 1; i < words.length; i++) {
            tag.append(Character.toUpperCase(words[i].charAt(0)));
            tag.append(words[i].substring(1).toLowerCase());
        }

        return tag.substring(0, Math.min(100, tag.length()));
    }
}
