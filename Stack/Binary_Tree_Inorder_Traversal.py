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

s = Solution1()
print(s)


def pre_order(tree):
    if tree == None:
        return
    print(tree.data)
    pre_order(tree.left)
    pre_order(tree.right)

def mid_order(tree):