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
linked_list = LinkedList()

# Menambahkan node baru di awal
print('Menambah angka 5 di awal list')
linked_list.AtBegining(5)
linked_list.PrintLinkedList()  # Output: 5

# Menambahkan node baru di akhir
print('\nmenambahkan angka 10 diakhir list')
linked_list.AtEnd(10)
linked_list.PrintLinkedList()  # Output: 5, 10

# Menambahkan node baru setelah node tertentu
print('\nMenambahkan angka 7 setelah 5')
node_now = linked_list.head
x = [6, 7, 8, 9, 2]
for i in x:
    linked_list.Inbetween(node_now, i)
    node_now = node_now.pointer
linked_list.PrintLinkedList()  

# Menghapus node dengan nilai tertentu
print('\nMenghapus angka 2')
linked_list.RemoveNode(2)
linked_list.PrintLinkedList()  # Output: 5, 10
