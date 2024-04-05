class Node():
    def __init__(self, data, pointer=None):
        self.data = data
        self.pointer = pointer
    
class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def PrintLinkedList(self):
        printval = self.head
        post = 0
        while printval is not None:
            print([post], printval.data, "<- Head") if(post == 0) else print([post], printval.data)
            printval = printval.pointer
            post = post + 1

    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        NewNode.pointer = self.head
        self.head = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        laste = self.head
        while(laste.pointer != None):
            laste = laste.pointer
        laste.pointer = NewNode

    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("middle_node belum di isi")
            return
        NewNode = Node(newdata)
        NewNode.pointer = middle_node.pointer
        middle_node.pointer = NewNode

    def RemoveNode(self, Removekey):
        HeadVal = self.head

        if(HeadVal.data is not None):
            if(HeadVal.data == Removekey):
                self.head = HeadVal.pointer
                HeadVal = None
                return
            
        while(HeadVal is not None):
            if HeadVal.data == Removekey:
                break    
            prev = HeadVal
            HeadVal = HeadVal.pointer
        if(HeadVal == None):
            return
        prev.pointer = HeadVal.pointer
        HeadVal = None

    def Search(self, val):
        current = self.head
        post = 0
        while current:
            if current.data == val:
                print([post])
                return [post]
            current = current.pointer
            post = post + 1
        print(False)
        return False
