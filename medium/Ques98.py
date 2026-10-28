# 98. Validate Binary Search Tree
# in python
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def check(node, low, high):
            if not node:
                return True

            if not low < node.val < high:
                return False

            return check(node.left, low, node.val) and \
                   check(node.right, node.val, high)

        return check(root, float('-inf'), float('inf'))


# in java
class Solution {
    public boolean isValidBST(TreeNode root) {
        return validBST(root, null, null);
    }

    private boolean validBST(TreeNode root, TreeNode min, TreeNode max) {
        if (root == null)
            return true;

        if (min != null && root.val <= min.val)
            return false;
        else if (max != null && root.val >= max.val)
            return false;

        return validBST(root.left, min, root) && validBST(root.right, root, max);
    }
}
