class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while start.next != None:
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        ptr1 = head
        while ptr1 and ptr1.next:
            ptr2 = ptr1
            while ptr2.next:
                if ptr1.data == ptr2.next.data:
                    dup = ptr2.next
                    ptr2.next = ptr2.next.next
                    del dup
                else:
                    ptr2 = ptr2.next
            ptr1 = ptr1.next
        return head
        
mylist = Solution()
t = int(input())
head = None
for i in range(t):
    data = int(input())
    head = mylist.insert(head, data)
head= mylist.removeDuplicates(head)
mylist.display(head)
