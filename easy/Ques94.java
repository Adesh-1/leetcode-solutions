// 94. Binary Tree Inorder Traversal
// in java
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        inorder(root, list);
        return list;
    }
    private void inorder(TreeNode root, List<Integer> list){
        if (root == null)
            return;

        inorder(root.left, list);
        list.add(root.val);
        inorder(root.right, list);
    }
}

// in python
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        l = []
        self.inorder(root, l)
        return l

    def inorder(self, root, l):
        if root == None:
            return

        self.inorder(root.left, l)
        l.append(root.val)
        self.inorder(root.right, l)
