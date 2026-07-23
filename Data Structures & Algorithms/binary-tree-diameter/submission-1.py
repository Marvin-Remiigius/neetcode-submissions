class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def height(node):
            if not node:
                return -1        # height in edges

            left = height(node.left)
            right = height(node.right)

            self.diameter = max(self.diameter, left + right + 2)

            return max(left, right) + 1

        height(root)
        return self.diameter