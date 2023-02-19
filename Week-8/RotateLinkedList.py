class node:

    def __init__ (self,data):
        self.data = data
        self.next = None

class linkedlist:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def addlast(self,data):
        if (self.head==None):
            self.head = self.tail = node(data)
        else:
            a = node(data)
            self.tail.next = a
            self.tail = a

    def printlist(self):
        current = self.head
        while (current != None):
            print(current.data,"-->",end="")
            current = current.next
        print("NUll")

    def rotatelist(self):
        k = 2 
        while k:
            current = self.head.next    
            previous = self.head
            
            while(current.next):
                current = current.next
                previous = previous.next
    
            current.next = self.head
            self.head= current
            previous.next = None
            k-=1
            if k<=0:
                break
        

obj = linkedlist()
obj.addlast(1)
obj.addlast(2)
obj.addlast(3)
obj.addlast(4)
obj.addlast(5)
obj.rotatelist()
obj.printlist()

### Time Complexity: O(N) and Space: O(1)