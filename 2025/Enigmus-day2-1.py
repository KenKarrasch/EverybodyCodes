import re
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value  # value will be [number, letter]
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, number, letter):
        """Insert a [number, letter] pair into the BST"""
        new_node = TreeNode([number, letter])
        if self.root is None:
            self.root = new_node
        else:
            self._insert_helper(self.root, new_node)
    
    def _insert_helper(self, current, new_node):
        """Recursive helper for insertion"""
        if new_node.value[0] < current.value[0]:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_helper(current.left, new_node)
        elif new_node.value[0] > current.value[0]:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_helper(current.right, new_node)
        else:
            # Handle duplicate numbers (you can modify this behavior)
            current.value[1] = new_node.value[1]  # Update the letter
    
    def search(self, number):
        """Search for a number in the BST, returns [number, letter] or None"""
        return self._search_helper(self.root, number)
    
    def _search_helper(self, node, number):
        if node is None:
            return None
        if number == node.value[0]:
            return node.value
        elif number < node.value[0]:
            return self._search_helper(node.left, number)
        else:
            return self._search_helper(node.right, number)
    
    def delete(self, number):
        """Delete a node with the given number"""
        self.root = self._delete_helper(self.root, number)
    
    def _delete_helper(self, node, number):
        if node is None:
            return node
        
        if number < node.value[0]:
            node.left = self._delete_helper(node.left, number)
        elif number > node.value[0]:
            node.right = self._delete_helper(node.right, number)
        else:
            # Node found - handle deletion
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Node has two children
                successor = self._find_min(node.right)
                node.value = successor.value
                node.right = self._delete_helper(node.right, successor.value[0])
        return node
    
    def _find_min(self, node):
        """Find the node with minimum value in a subtree"""
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def inorder_traversal(self):
        """In-order traversal returns sorted pairs"""
        result = []
        self._inorder_helper(self.root, result)
        return result
    
    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)
    
    def preorder_traversal(self):
        """Pre-order traversal"""
        result = []
        self._preorder_helper(self.root, result)
        return result
    
    def _preorder_helper(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_helper(node.left, result)
            self._preorder_helper(node.right, result)
    
    def postorder_traversal(self):
        """Post-order traversal"""
        result = []
        self._postorder_helper(self.root, result)
        return result
    
    def _postorder_helper(self, node, result):
        if node:
            self._postorder_helper(node.left, result)
            self._postorder_helper(node.right, result)
            result.append(node.value)
    
    def height(self):
        """Calculate the height of the tree"""
        return self._height_helper(self.root)
    
    def _height_helper(self, node):
        if not node:
            return 0
        return 1 + max(self._height_helper(node.left), self._height_helper(node.right))
    
    def size(self):
        """Count the number of nodes in the tree"""
        return self._size_helper(self.root)
    
    def _size_helper(self, node):
        if not node:
            return 0
        return 1 + self._size_helper(node.left) + self._size_helper(node.right)

    def get_letters_at_level(self, level):
        """
        Returns a list of letters at the specified level (0-based)
        Returns empty list if level doesn't exist
        """
        if self.root is None:
            return []
        
        result = []
        current_level = 0
        queue = deque([(self.root, current_level)])
        
        while queue:
            node, node_level = queue.popleft()
            
            if node_level == level:
                result.append(node.value[1])  # Add the letter to result
            elif node_level > level:
                break  # We've passed our target level
            
            # Add children to queue with their correct level
            if node.left:
                queue.append((node.left, node_level + 1))
            if node.right:
                queue.append((node.right, node_level + 1))
        
        return result


# Example usage
if __name__ == "__main__":

    f = open('day2-1.txt').read().split('\n')

    # Create a binary tree
    bstl = BST()
    bstr = BST()


    for i in f:
        bts = i.split()[2:4]        
        num = int(re.findall(r'\d+', bts[0])[0])    
        #ltr = re.findall(r'[A-Z]', bts[0])[0]            
        ltr = bts[0].split(',')[1].replace(']','')
        bstl.insert(num,ltr)
        num = int(re.findall(r'\d+', bts[1])[0])    
        ltr = bts[1].split(',')[1].replace(']','')
        #ltr = re.findall(r'[A-Z]', bts[1])[0]            
        bstr.insert(num,ltr)
        print(num,ltr)
        

    lcode = []

    for i in range(bstl.height()):
        ncode = bstl.get_letters_at_level(i)
        if len(ncode) > len(lcode):
            lcode = ncode[:]
    rcode = []
    for i in range(bstr.height()):
        ncode = bstr.get_letters_at_level(i)
        if len(ncode) > len(rcode):
            rcode = ncode[:]
    
    print("In-order (sorted):", bstr.inorder_traversal())
    print("Pre-order:", bstr.preorder_traversal())
    print("Post-order:", bstr.postorder_traversal())

    print(lcode)
    print(rcode)
    print(''.join(lcode + rcode))
