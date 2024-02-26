inorder = []
preorder = []
postorder = []

class NodeMaker:
    def __init__(self, key):
        self.l = None
        self.r = None
        self.v = key

def insert(root, key):
    if root is None:
        return NodeMaker(key)
    else:
        if root.v == key:
            root.r = insert(root.l, key)
        elif root.v < key:
            root.r = insert(root.r, key)
        else:
            root.l = insert(root.l, key)
    return root
 
def printInorder(root):
 
    if root:
 
        printInorder(root.l)
        inorder.append(root.v)
        printInorder(root.r)

def printPreorder(root):
 
    if root:
 
        preorder.append(root.v)
        printPreorder(root.l)
        printPreorder(root.r) 
 
def printPostorder(root):
 
    if root:

        printPostorder(root.l)
        printPostorder(root.r)
        postorder.append(root.v)
 

if __name__ == "__main__":

    ins = "BINARYSEARCHTREE"

    root = NodeMaker(ins[0])
    for i in range(len(ins)-1):
        root = insert(root, ins[i+1])
 
    printInorder(root)
    
    printPreorder(root)

    printPostorder(root)


    inorderstr = ''.join(inorder)
    preorderstr = ''.join(preorder)
    postorderstr = ''.join(postorder)
    output = preorderstr+ " " + postorderstr
    print(inorderstr)
    print(output)