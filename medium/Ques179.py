# 179. Largest Number
# in python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = list(map(str, nums))

        def compare(a, b):
            if a + b > b + a:
                return -1
            return 1

        arr.sort(key=cmp_to_key(compare))

        if arr[0] == "0":
            return "0"

        return "".join(arr)

# in java
class Solution {
    public String largestNumber(int[] nums) {
        String[] arr = new String[nums.length];

        for (int i = 0; i < nums.length; i++)
            arr[i] = String.valueOf(nums[i]);

        Arrays.sort(arr, (a, b) -> (b + a).compareTo(a + b));

        if (arr[0].equals("0"))
            return "0";

        StringBuilder sb = new StringBuilder();

        for (String s : arr)
            sb.append(s);

        return sb.toString();
    }
}
