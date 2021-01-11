class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = node()

    def append(self, data):
        newNode = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = newNode

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_Node = self.head
        while cur_Node.next != None:
            cur_Node = cur_Node.next
            elems.append(cur_Node.data)
        print(elems)
    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range")
            return 
        cur_idx = 0
        cur_Node = self.head
        while True:
            if cur_idx == index: return cur_Node.data
            cur_idx += 1
    def erase(self):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range")
            return 
        cur_idx = 0
        cur_Node = self.head
        while True:
            lastNode = cur_Node
            cur_Node = cur_Node.next
            if cur_idx == index:
                lastNode.next = cur_Node.next
                return
            cur_idx += 1

k = linkedList()
k.append(1)
k.display()

        
