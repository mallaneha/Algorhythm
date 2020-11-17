class BinarySearchTree:
    def __init__(self):
        self.BSTsize = 0
        self.root = None
    

    class BSTnode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None


    # Add a node to the BST
    def add(self, key, value):
        newNode = self.BSTnode(key, value)
        self.BSTsize += 1

        if self.root == None:
            self.root = newNode
        else:
            node = self.root
            while node != None:
                if key <= node.key:
                    if node.left == None:
                        node.left = newNode
                        break
                    else:
                        node = node.left
                else:
                    if node.right == None:
                        node.right = newNode
                        break
                    else:
                        node = node.right
    

    # Return the number of nodes in the BST
    def size(self):
        return self.BSTsize


    # Perform inorder traversal. Must return a list of keys visited in inorder way, e.g. [1, 2, 3, 4].
    def inorder_walk(self):
        return self.inorder(self.root, [])        


    def inorder(self, root, inList):
        if root != None:
            self.inorder(root.left, inList)
            inList.append(root.key)
            self.inorder(root.right, inList)
        return inList


    # Perform postorder traversal. Must return a list of keys visited in inorder way, e.g. [1, 4, 3, 2].
    def postorder_walk(self):
        return self.postorder(self.root, [])
    
    
    def postorder(self, root, postList):
        if root != None:
            self.postorder(root.left, postList)
            self.postorder(root.right, postList)
            postList.append(root.key)
        return postList


    # Perform preorder traversal. Must return a list of keys visited in inorder way, e.g. [2, 1, 3, 4].
    def preorder_walk(self):
        return self.preorder(self.root, [])
    
    
    def preorder(self, root, preList):
        if root != None:
            preList.append(root.key)
            self.preorder(root.left, preList)
            self.preorder(root.right, preList)
        return preList


    # Search the BST for the given key. Return False if the key is not found.
    def search(self, key):
        root = self.root

        while root != None:
            if key == root.key:
                return root.value
            elif key < root.key:
                root =  root.left
            else:
                root = root.right
        return False


    # Remove a key from the BST. Return False if the key is not present in the BST.
    def remove(self, key):
        # root: node to be deleted, element: node to be swapped with root
        root = self.root

        while root != None:# searching the node
            if key == root.key:
                break
            parent = root# parent of the node to be removed
            if key < root.key:
                root =  root.left
                child = "left"
            else:
                root = root.right
                child = "right"

        if root != None:
            self.BSTsize -= 1
            if root.left == None and root.right == None:# node is a leaf node
                if self.root == root:
                    self.root = None
                elif child == "left":
                    parent.left = None
                elif child == "right":
                    parent.right = None

            elif root.left == None and root.right != None:# node has right subtree only
                if self.root == root:
                    self.root = root.right
                elif child == "left":
                    parent.left = root.right
                elif child == "right":
                    parent.right = root.right

            elif root.left != None and root.right == None:# node has a left subtree only
                if self.root == root:
                    self.root = root.left
                elif child == "left":
                    parent.left = root.left
                elif child == "right":
                    parent.right = root.left

            else:# node has both children
                # finding 'element' that is the largest node from left subtree of the node to be removed 
                element = root.left
                
                while element.right != None:
                    parentElement = element# parent of element
                    element = element.right

                #replacing the node with element                
                root.key = element.key
                root.value = element.value

                if root.left == element:# largest element in the left subtree is the left child of the node itself
                    root.left = element.left
                else:
                    if element.left == None:# largest element node has no left subtree
                        parentElement.right = None
                    else:
                        parentElement.right = element.left
        else:
            return False


    # Find the smallest key and return the corresponding key-value pair/tuple, i.e. (key, value)
    def smallest(self):
        root = self.root

        while root.left != None:
            root = root.left
        return root.key, root.value


    # Find the largest key and return the corresponding key-value pair/tuple, i.e. (key, value)
    def largest(self):
        root = self.root

        while root.right != None:
            root = root.right
        return root.key, root.value
