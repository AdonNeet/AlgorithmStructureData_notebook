# L200220194
class Node(object):
    """sebuah simpul di linked list"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def kunjungi(head):
    curNode = head
    while curNode is not None:
        print(curNode.data)
        curNode = curNode.next

# Tugas 3
def cari(head, data):
    curNode = head
    while curNode is not None:
        if curNode.data == data:
            return curNode
        curNode = curNode.next
    return "Tidak ada"

def tambahDepan(head, data):
    newNode = Node(data)
    newNode.next = head
    return newNode

def tambahAkhir(head, data):
    if head is None:
        return Node(data)
    curNode = head
    while curNode.next is not None:
        curNode = curNode.next
    curNode.next = Node(data)
    return head

def tambah(head, data, posisi):
    if posisi == 0:
        return tambahDepan(head, data)
    curNode = head
    for _ in range(posisi):
        if curNode is None:
            return head
        curNode = curNode.next
    if curNode is None:
        return head
    newNode = Node(data)
    newNode.next = curNode.next
    curNode.next = newNode
    return head

def hapus(head, posisi):
    if head is None:
        return None
    if posisi == 0:
        return head.next
    curNode = head
    prevNode = None
    for _ in range(posisi):
        if curNode is None:
            return head
        prevNode = curNode
        curNode = curNode.next
    if curNode is None:
        return head
    prevNode.next = curNode.next
    return head
