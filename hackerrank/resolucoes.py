def insert(self,head,data):
    if (head == None):
        head = Node(data)
    elif (head.next == None):
        head.next = Node(data)
    else:
        self.insert(head.next, data)
    return head

#
# The function gets called with the whole linked list.
#     If the list is empty,
#     	insert the element as the head.
#     Otherwise if there is no element after the head,
#     	put the data after the head.
#     Otherwise,
#     	call the function with all of the elements except for the current head