# https://www.hackerrank.com/challenges/30-linked-list/problem
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    tail = None

    def insert(self, head, data):  # quicker n(1)
        # print(data) #cheating way
        if not head:
            head = Node(data)
            self.tail = head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        return head

    # def insert(self, head, data): #slower method O(n)
    #     if not head:
    #         head = Node(data)
    #     else:
    #         current = head
    #         while current.next:
    #             current = current.next
    #         current.next = Node(data)
    #     return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
