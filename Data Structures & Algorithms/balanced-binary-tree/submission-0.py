class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            if left == -1:
                return -1  # left subtree unbalanced

            right = dfs(node.right)
            if right == -1:
                return -1  # right subtree unbalanced

            # FIX: correct balance condition
            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        # tree is balanced if dfs(root) does NOT return -1
        return dfs(root) != -1
