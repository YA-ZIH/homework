import queue

class HuffmanNode(object):
    def __init__(self, left=None, right=None, root=None):
        self.left = left
        self.right = right
        self.root = root     
    def children(self):
        return((self.left, self.right))
    def preorder(self,path=None):
        if path is None:
            path = []
        if self.left is not None:
            if isinstance(self.left[1], HuffmanNode):
                self.left[1].preorder(path+[0])
            else:
                print(self.left,path+[0])
        if self.right is not None:
            if isinstance(self.right[1], HuffmanNode):
                self.right[1].preorder(path+[1])
            else:
                print(self.right,path+[1])
freq = [
    (0.25, 'a'), (0.25, 'b'), (0.125, 'c'), (0.125, 'd'),
    (0.125, 'e'),(0.0625, 'f'), (0.0625, 'g') ]
def encode(frequencies):
    def __lt__(self,other):
        return 0
    p = queue.PriorityQueue()
    for item in frequencies:
        p.put(item)
    while p.qsize() > 1:
        left,right = p.get(),p.get()
        node = HuffmanNode(left,right)
        p.put((left[0]+right[0],node))
    return p.get()
node = encode(freq)
print(node[1].preorder())