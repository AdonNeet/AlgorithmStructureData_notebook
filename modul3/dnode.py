# L200220194
# Tugas 4
class DNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def kunjungi_depan(head):
    curNode = head
    while curNode is not None:
        print(curNode.data)
        curNode = curNode.next

def kunjungi_belakang(tail):
    curNode = tail
    while curNode is not None:
        print(curNode.data)
        curNode = curNode.prev

def tambahDepan(head, data):
    newNode = DNode(data)
    newNode.next = head
    if head:
        head.prev = newNode
    return newNode

def tambahAkhir(tail, data):
    newNode = DNode(data)
    if tail:
        tail.next = newNode
        newNode.prev = tail
    return newNode
