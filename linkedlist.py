class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    

    def insert_at_begin(self,data):
        node= Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print(" list is empty")
            return 
        lstr=''
        current=self.head
        while current is not None:
            lstr += str(current.data) + '-->'
            current=current.next

        print(lstr)

    def insert_at_end(self,data):
        if self.head is None:
            node=Node(data,None)
            self.head=node
            return
        current=self.head
        print(current)
        while current.next is not None:
            current=current.next
        
        node=Node(data,None)
        current.next=node

    def get_length(self):
        count=0
        current=self.head
        while current is not None:
            count=count+1
            current=current.next
        return count

    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head=self.head.next
            return
        current=self.head
        count=0
        while current is not None:
            if count == index - 1:
                current.next=current.next.next
                break
            
            current=current.next
            count+=1
    def insert_values(self,data_list):
        self.head=None
        for i in data_list:
            self.insert_at_end(i)

    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception ("Invalid index")
        
        if index == 0:
            node=Node(data,self.head)
            self.head=node
            return
        
        current=self.head
        count = 0
        while current is not None:
            if count == index - 1:
                node=Node(data,current.next)
                current.next=node
                #node.next=current.next
                break
            
            current=current.next
            count+=1

    def insert_after_value(self,data_after,data_insert):

        current=self.head
        while current is not None:
            if current.data == data_after:
                node = Node(data_insert,current.next)
                current.next=node
                break
            
            current=current.next

    def remove_by_value(self,data_toremove):
        current=self.head

        while current.next is not None:
            if current.next.data == data_toremove:
                current.next=current.next.next
            
            current=current.next

        

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","apple","mango","plums"])
    ll.print()
    ll.insert_after_value("apple","jackfruit")
    ll.print()
    ll.remove_by_value("apple")
    """ ll.insert_at_begin(3)
    ll.insert_at_begin(5)
    ll.insert_at_end(4) """
    ll.print()
    #print(" The total number of elements in the linkedlist is ", ll.get_length())
