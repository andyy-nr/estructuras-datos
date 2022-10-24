from clases import Graph as G, TreeNode as T

# Creates a graph where the edges have weight
gdict = {"sf": [["la", 1000]],
         "la": [["lv", 390], ["sf", 1000]],
         "lv": [["la", 390], ["kc", 3000]],
         "kc": [["ny", 3500], ["la", 2000], ["lv", 3000]],
         "ny": [["kc", 2000], ["sf", 1500]],
         }

graph = G(gdict)
# Trying to remove an element
print(graph.remove_element("sf"))
print(graph.dict)

root = T(27)
root.insert(14)
root.insert(35)
root.insert(19)
root.insert(10)
root.insert(15)
root.insert(31)
root.insert(42)

# root.printTree()
print(root.inOrder(root))  # left, root, right
print(root.postOrder(root))  # left, right, root
print(root.preOrder(root))  # root, left, right
root = root.delete_element(root, 35)
print("After deleting the element")
print(root.inOrder(root))
min = root.min(root)
max = root.max(root)

print(f"El valor maximo es {max.data}, el valor minimo es {min.data}")