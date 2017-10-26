'''和雍祥的共同成果'''
import queue

class HuffmanNode(object):                  # Huffman 演 算 法
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
    def __lt__(self,other):                     # 1.  創 造 每 個 的 leaf node
        return 0                                
    p = queue.PriorityQueue()                   #     然 後 把 他 加 到 優 先 序 列 ( priority queue )
    for item in frequencies:                    
        p.put(item)                             
    while p.qsize() > 1:                        # 2.  如 果 有 大 於 一 個 節 點 就 會 繼 續 做
        left,right = p.get(),p.get()            # 2a. 移 除 掉 兩 最 大 的 節 點
        node = HuffmanNode(left,right)          # 2b. 內 部 的 節 點 當 成 子
        p.put((left[0]+right[0],node))          # 2c. 增 加 新 的 節 點 到 這 個 序 列
    return p.get()                              # 3.  樹 完 成 ， 回 傳 根 部 節 點
node = encode(freq)
print(node[1].preorder())
