# 1773. Count Items Matching a Rule
# in py
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        if ruleKey == "type":
            index = 0
        elif ruleKey == "color":
            index = 1
        elif ruleKey == "name":
            index = 2

        # for i in range(len(items)):
        #     if items[i][index] == ruleValue:
        #         count += 1

        for item in items:
            if item[index] == ruleValue:
                count += 1
        return count

  # in java
  class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int count = 0, index = 0;
         if (ruleKey.equals("type")) {
            index = 0;
        } else if (ruleKey.equals("color")) {
            index = 1;
        } else if (ruleKey.equals("name")) {
            index = 2;
        }
        for(List<String> s : items){
            if(s.get(index).equals(ruleValue))
                count++;
        }
        return count;
    }
}
