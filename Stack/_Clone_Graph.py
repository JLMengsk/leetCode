# -*- coding:utf-8 -*-
# @Time     : 6/25/2020 5:20 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Clone_Graph.py
# @Software : PyCharm

# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# DFS  SU1
class Solution1:
    map = dict()

    def cloneGraph(self, node):
        if not node:
            return node
        self.map[node] = Node(node.val, [])
        for n in node.neighbors:
            if n in self.map.keys():
                self.map[node].neighbors.append(self.map[n])
            else:
                self.map[node].neighbors.append(self.cloneGraph(n))
        return self.map[node]

# DFS  SU2
# class Solution2:
#     def cloneGraph(self, node):
#         if not node:
#             return None
#         if len(node.neighbors) == 0:
#             return Node(node.val)
#         seenDict = {}
#         stack = [node]
#         visited = {}
#         while stack:
#             currNode = stack.pop(0)
#             if currNode in visited:
#                 continue
#             if currNode not in seenDict:
#                 newNode = Node(currNode.val)
#                 seenDict[currNode] = newNode
#             else:
#                 newNode = seenDict[currNode]
#             for neighbor in currNode.neighbors:
#                 if neighbor in seenDict:
#                     newNode.neighbors.append(seenDict[neighbor])
#                 else:
#                     temp = Node(neighbor.val)
#                     newNode.neighbors.append(temp)
#                     seenDict[neighbor] = temp
#                 stack.append(neighbor)
#             visited[currNode] = 1
#         return seenDict[node]