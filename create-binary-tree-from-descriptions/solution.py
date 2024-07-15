# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        inEdges = defaultdict(list)
        outEdges = defaultdict(list)
        for parent, child, isLeftChild in descriptions:
            inEdges[child].append(parent)
            outEdges[parent].append([child, isLeftChild])
        root = None
        for parent in outEdges:
            if parent not in inEdges:
                root = TreeNode(parent)
        def dfs(root):
            for child, isLeftChild in outEdges[root.val]:
                node = TreeNode(child)
                if isLeftChild == 1:
                    root.left = node
                else:
                    root.right = node
                dfs(node)
        dfs(root)
        return root
