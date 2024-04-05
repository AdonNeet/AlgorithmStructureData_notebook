class Node():
    def __init__(self, data, pointer=None):
        self.data = data
        self.pointer = pointer
    
class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def PrintLinkedList(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.pointer

    def Count(self):
        post = self.head
        ans = 0
        while post is not None:
            ans += post.data
            post = post.pointer
        print(ans)

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

# Membuat instance LinkedList
nodTemp = Node(3, Node(5, Node(2, Node(6, Node(9, Node(7))))))
linked_list = LinkedList(nodTemp)
print('Berikut merupakan list yang telah dibuat')
linked_list.PrintLinkedList()
print('\nBerikut merupakan jumlah dari list angka diatas')
linked_list.Count()

