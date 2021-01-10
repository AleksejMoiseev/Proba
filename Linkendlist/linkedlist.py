"""
Имплементация LinkedList
"""


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = Node()

    def __str__(self):
        linked_list_str = ""
        idx = 0
        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next
            idx += 1
            linked_list_str = linked_list_str + f"{idx}: {pointer.data} , "
        return linked_list_str

    def get_last(self):
        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next
        return pointer

    def append(self, data):
        new_node = Node(data=data)
        last = self.get_last()
        last.next = new_node

    def print(self):
        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next
            print(pointer.data)

    def length(self):
        idx = 0
        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next
            idx += 1
        return idx

    def set(self, index, data):
        idx = 0
        pointer = self.head
        while idx < index:
            pointer = pointer.next
            idx += 1
        pointer.data = data

    def _get(self, index):
        idx = 0
        pointer = self.head
        while idx < index:
            pointer = pointer.next
            idx += 1
        return pointer

    def get(self, index):
        idx = 0
        pointer = self.head
        while idx < index:
            pointer = pointer.next
            idx += 1
        return pointer.data

    def erase(self, index):
        if index == 0:
            prev = self.head
        else:
            prev = self._get(index=(index-1))
        to_del = prev.next
        prev.next = to_del.next
        data = to_del.data
        del to_del
        return data


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(data="Fedor")
    ll.append(data="Julia")
    # print(ll.get(2))
    ll.set(index=1, data="fedul")
    print(ll.erase(1))
    print(ll)
    # ll.print()
    # print(ll.length())