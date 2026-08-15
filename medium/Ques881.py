# 881. Boats to Save People
# in python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        boats = 0

        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
                
            j -= 1
            boats += 1

        return boats

# in java
class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int i = 0, j = people.length - 1;
        int boats = 0;

        while (i <= j) {
            if (people[i] + people[j] <= limit)
                i++;
            j--;
            boats++;
        }
        return boats;
    }
}
