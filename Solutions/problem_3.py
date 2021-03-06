class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
        self.is_locked = False

    def populate(self, node_value):    # inserting nodes into the tree
        if self.data:
            if node_value < self.data:
                if self.left is None:
                    self.left = Node(node_value)
                else:
                    self.left.populate(node_value)
                    
            elif node_value > self.data:
                if self.right is None:
                    self.right = Node(node_value)
                else:
                    self.right.populate(node_value)
        else:
            self.data = node_value


ancestors_locklist =[]
descendents_locklist = []

def getAncestorsStatus(root, node):
    global ancestors_locklist

    if root:
        if root.data == node:       # node found in tree
            getDescendentsStatus(root, node)    # get descendents status as well
            return True

        left = getAncestorsStatus(root.left, node)          #search left hand side of tree
        if not left:                                        #node not found in left_Tree
            right = getAncestorsStatus(root.right, node)    #search right_Tree

        if left or right:           
            ancestors_locklist.append(root.is_locked)


def getDescendentsStatus(root, node):
    global descendents_locklist

    if root is None:
        return False

    left = getDescendentsStatus(root.left, node)
    if not left:
        right = getDescendentsStatus(root.right, node)

    if root.data != node:
        descendents_locklist.append(root.is_locked)


def lock(listA):
    if 'True' in listA:       # List contains node with is_locked = True
        return False
    else:
        return True
        

def unlock(listB):
    if 'True' in listB:
      return False
    else:
        return True


def lockNode(root, node):
    if root:
        if root.data == node:  # node found in tree
            print ("found in locknode function")
            root.is_locked = True
    
        lockNode(root.left, node)       # search left Tree
        lockNode(root.right, node)      # search right Tree


if __name__ == '__main__':
    root = Node(30)           # insert root node
    root.populate(10)         # insert other nodes
    root.populate(50)
    root.populate(5)
    root.populate(15)
    root.populate(40)
    root.populate(60)
    
    getAncestorsStatus(root, 10)    # find the ancestors and descendants of node_value 10
    
    if lock(ancestors_locklist) and lock(descendents_locklist):
        lockNode(root, 10)          # lock the node when all the ancestors and descendants nodes are unlocked

    getAncestorsStatus(root, 5)
    print(ancestors_locklist)       # will be able to see the is_locked status of anscestor node 10 is now set to True
