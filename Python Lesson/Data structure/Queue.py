from Linkendlist.linkedlist import LinkedList


class Queue:

    def __init__(self):
        self.linked_list = LinkedList()

    def enqueue(self, data):
        self.linked_list.append(data=data)

    def dequeue(self):
        return self.linked_list.erase(index=1)

    def front(self):
        return self.linked_list.get(index=1)

    def back(self):
        return self.linked_list.get_last().data

    def __str__(self):
        return self.linked_list.__str__()


if __name__ == '__main__':
    q = Queue()
    q.enqueue("fedor")
    q.enqueue("julia")
    print(q.front())
    print(q.back())
    print(q.dequeue())
    print(q)
