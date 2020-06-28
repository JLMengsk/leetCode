# -*- coding:utf-8 -*-
# @Time     : 6/26/2020 7:50 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Binary_Tree_Inorder_Traversal.py
# @Software : PyCharm

# Given a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root):
        ans = []
        cur = root
        stack = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            ans.append(node.val)
            cur = node.right
        return ans


s = Solution()
print(s)

"""
Recursive solution

def pre_order(tree):
    if tree == None:
        return
    print(tree.data)
    pre_order(tree.left)
    pre_order(tree.right)

def mid_order(tree):
    if tree == None:
        return
    mid_order(tree.left)
    print(tree.data)
    mid_order(tree.right)

def post_order(tree):
    if tree == None:
        return
    post_order(tree.left)
    post_order(tree.right)
    print(tree.data)
    
##############################################################
    
Non-Recursive way

def preOrder(self,root):
    if root == None:
        return
    myStack = []
    ans = []
    node = root
    while node or myStack:
        while node:
            ##### ans.append(node.val) ####
            myStack.append(node)
            node = node.lchild
        node = myStack.pop()
        node = node.rchild
        

def inOrder(self,root):
    if root == None:
        return
    myStack = []
    ans = []
    node = root
    while node or myStack:
        while node:
            myStack.append(node)
            node = node.lchild
        node = myStack.pop()
        #### ans.append(node.val) ####
        node = node.rchild


def postOrder1(self,root):
    if not root:
        return
    myStack = []
    markNode = None
    ans = []
    node = root
    while node or myStack:
        while node:
            myStack.append(node)
            node = node.lchild
        node = myStack.pop()
        if not node.rightNode or node.rightNode is markNone:
        #node  has no rightNode or node's rightNode has been checked 
            ans.append(val.val)
            markNode = node
            node = None
        else:
            myStack.append(node)
            node = node.right
            
            
def postOrder2(self,root):
    if not root:
        return []
    myStack = []
    ans = []
    while node_stack:
        node = node_stack.pop()
        if node.left:
            node_stack.append(node.left)
        if node.right:
            node_stack.append(node.right)
        ans.append(node.val)
    return ans[::-1]
"""
