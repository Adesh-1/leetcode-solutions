# 1023. Camelcase Matching
# in python
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        return [self.checkCase(query, pattern) for query in queries]

    def checkCase(self, query: str, pattern: str) -> bool:
        j = 0

        for ch in query:
            if j < len(pattern) and ch == pattern[j]:
                j += 1
            elif ch.isupper():
                return False

        return j == len(pattern)

# in java
class Solution {
    public List<Boolean> camelMatch(String[] queries, String pattern) {
        List<Boolean> ans = new ArrayList<>();

        for (String query : queries) {
            ans.add(checkCase(query, pattern));
        }
        return ans;
    }

    private boolean checkCase(String query, String pattern) {
        int j = 0;

        for (char ch : query.toCharArray()) {
            if (j < pattern.length() && ch == pattern.charAt(j))
                j++;
            else if (Character.isUpperCase(ch))
                return false;
        }

        return j == pattern.length();
    }
}
