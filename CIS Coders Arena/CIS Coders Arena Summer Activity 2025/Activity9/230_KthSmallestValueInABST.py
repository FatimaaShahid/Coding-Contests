# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def kthSmallest(root, k):
    val = []

    def traverse(root):
        if root == None:
            return
        val.append(root.val)
        traverse(root.left)
        traverse(root.right)
        return
    
    traverse(root)
    val.sort()
    return val[k-1]
        
        