# Linked List
class Node:
    def __init__(self, data):
        self.dataval = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self, node):
        val = node
        while val is not None:
            print(val)
            val = val.next

# Grafos

class Graph:
    def __init__(self, dict = None):
        if dict is None:
            dict = []
        self.dict = dict

    def show_vrtx(self):
        return list(self.dict.getkeys())

    def get_edges(self):
        list_edges = []
        for vtxname in self.dict:
            for edge in self.dict[vtxname]:
                if {vtxname, edge[0]} not in list_edges:
                    list_edges.append({vtxname, edge[0]})
        return list_edges

    def edges(self):
        return self.get_edges()

    def get_edge_weight(self):
        list_weight = []
        for vtxname in self.dict:
            for edge in self.dict[vtxname]:
                if {f"{vtxname}, {edge[0]} Weight: {edge[1]}"} not in list_weight:
                    list_weight.append(f"{vtxname}, {edge[0]} Weight: {edge[1]}")
        return list_weight

    def add_vrtx(self, vrtx):
        if vrtx not in self.dict:
            self.dict[vrtx] = []

    def find_element(self, element):
        if element in self.dict:
            print(f"The element edges are: {self.dict[element]}")

    def remove_element(self, element):
        new_dict = {}
        for vtxname in self.dict: # Removes al edges connected to the element
            new_dict[vtxname] = []
            for edge in self.dict[vtxname]:
                if edge[0] != element:
                    new_dict[vtxname].append(edge)
        self.dict = new_dict

        if element in self.dict:  # Removes the element
            self.dict.pop(element)
            return self.dict

# Trees

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, value):
        if value < self.data:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        elif value > self.data:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
        else:
            self.data = value

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def inOrder(self, root):
        res = []
        if root:
            res = self.inOrder(root.left)
            res.append(root.data)
            res = res + self.inOrder(root.right)
        return res

    def preOrder(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preOrder(root.left)
            res = res + self.preOrder(root.right)
        return res

    def postOrder(self, root):
        res = []
        if root:
            res = self.postOrder(root.left)
            res = res + self.postOrder(root.right)
            res.append(root.data)
        return res

    def find_element(self, element):
        if element < self.data:
            if self.left is None:
                return str(self.data) + " Not Found"
            return self.left.find_element(element)
        elif element > self.data:
            if self.right is None:
                return str(self.data) + " Not Found"
            return self.right.find_element(element)
        else:
            return str(self.data) + " Found"

    def min(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def max(self, node):
        current = node

        while current.right is not None:
            current = current.right

        return current

    def delete_element(self, node, element):
        if node is None:
            return node

        if element < node.data:
            node.left = self.delete_element(node.left, element)
        elif element > node.data:
            node.right = self.delete_element(node.right, element)

        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp

            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.min(node.right)
            node.data = temp.data
            node.right = self.delete_element(node.right, temp.data)

        return node

