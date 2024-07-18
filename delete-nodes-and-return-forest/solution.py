class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        results = []
        delete_set = set(to_delete)
        def dfs(current, parent):
            if current.val in delete_set and parent:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            if current.val not in delete_set and not parent:
                results.append(current)
            if current.left:
                dfs(current.left, current if current.val not in delete_set else None)
            if current.right:
                dfs(current.right, current if current.val not in delete_set else None)
        dfs(root, None)
        return results