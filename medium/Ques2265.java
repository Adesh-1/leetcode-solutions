// 2265. Count Nodes Equal to Average of Subtree
// in java
class Solution {
    int ans = 0;

    public int averageOfSubtree(TreeNode root) {
        dfs(root);
        return ans;
    }

    private int[] dfs(TreeNode root) {
        if (root == null)
            return new int[] { 0, 0 };

        int[] left = dfs(root.left);
        int[] right = dfs(root.right);

        int sum = root.val + left[0] + right[0];
        int count = 1 + left[1] + right[1];

        if (sum / count == root.val)
            ans++;

        return new int[] { sum, count };
    }
}

// in java
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def dfs(root):
            nonlocal ans

            if root is None:
                return 0, 0

            left_sum, left_count = dfs(root.left)
            right_sum, right_count = dfs(root.right)

            total = root.val + left_sum + right_sum
            count = 1 + left_count + right_count

            if total // count == root.val:
                ans += 1

            return total, count

        dfs(root)
        return ans
