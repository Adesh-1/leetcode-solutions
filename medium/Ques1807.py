# 1807. Evaluate the Bracket Pairs of a String
# in python
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mp = dict(knowledge)
        ans = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                j = s.index(')', i)
                key = s[i + 1:j]

                ans.append(mp.get(key, '?'))
                i = j + 1
            else:
                ans.append(s[i])
                i += 1

        return ''.join(ans)

# in java
class Solution {
    public String evaluate(String s, List<List<String>> knowledge) {
        HashMap<String, String> map = new HashMap<>();
        for (List<String> pair : knowledge)
            map.put(pair.get(0), pair.get(1));

        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                int j = i + 1;
                while (s.charAt(j) != ')')
                    j++;

                String key = s.substring(i + 1, j);
                ans.append(map.getOrDefault(key, "?"));
                i = j;

            } else {
                ans.append(s.charAt(i));
            }
        }
        return ans.toString();
    }
}
