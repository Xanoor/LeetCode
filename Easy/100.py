class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.left or q.left:
            if p.left is None or q.left is None:
                return False
        if p.right or q.right:
            if p.right is None or q.right is None:
                return False
        if p.val != q.val:
            return False

        if p.left:
            if self.isSameTree(p.left, q.left) == False:
                return False
        if p.right:
            if self.isSameTree(p.right, q.right) == False:
                return False

        return True
    
# 0ms 12.52Mb