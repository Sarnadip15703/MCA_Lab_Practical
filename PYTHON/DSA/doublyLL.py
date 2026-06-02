class Node:
    def __init__(self,item):
        self.info=item
        self. next=None
        self.prev=None

class double_linklist:
    def __init__(self):
        self.start=None

    def insert_at_last(self,item):
        nd=Node(item)

        if self.start==None:
            self.start=nd
            return
        
        temp=self.start
        while temp.next!=None:
            temp=temp.next
        temp.next=nd
        nd.prev=temp


    def display(self):
        temp=self.start
        while temp!=None:
            print(temp.info,sep="  ",end=" -> ")
            temp=temp.next
        print("end")

    def insert_at_beggining(self,item):
        nd=Node(item)

        nd.next=self.start
        if self.start:
            self.start.prev=nd
        self.start=nd

    def insert_at_position(self,item,position):
        nd=Node(item)

        if position==0:
            self.insert_at_beggining(item)
            return
        
        else:

            temp=self.start
            i=0

            while temp.next!=None and i<position-1 :
                temp=temp.next
                i+=1

            nd.next=temp.next
            if temp.next!=None:
                temp.next.prev=nd
            
            nd.prev=temp

            if temp.next==None:
              temp.next=nd
              return
            
            temp.next=nd

    def insert_after_specific_item(self,item,find_item):

        nd=Node(item)
        temp=self.start

        while temp!=None and temp.info!=find_item :
               temp=temp.next
            
        if temp==None:
         print("Item not found")
         return
        
        nd.next=temp.next
        nd.prev=temp
        temp.next=nd
        if nd.next:
            nd.next.prev=nd


        
    def delete_last(self): 
        temp=self.start 
        while temp.next!=None:
              p=temp 
              temp=temp.next 
            
        temp.prev.next=None
        del temp

    def delete_first(self): 
        temp=self.start 
        self.start=temp.next 
        del temp

    def delete_specific_position(self,position):
      if position==0:
          self.delete_first()
          return
      temp=self.start
      i=0
      p=temp
      while temp.next!=None and i<position:
        p=temp
        temp=temp.next   #10 20 30 40
        i+=1
      
      p.next=temp.next
      if temp.next==None:
          self.delete_last()
          return
        
      temp.next.prev=p
      del temp

    def delete_specific_item(self,item):
        temp=self.start
        
        while(temp!=None and temp.info!=item):
            temp=temp.next

        if(temp == None):
            print("Item not found in the list")
            return

        if(temp.next==None):
            self.delete_last()
            return
        
        temp.prev.next=temp.next
        temp.next.prev=temp.prev
        del temp
            
          

dl=double_linklist()
dl.insert_at_last(10)
dl.insert_at_beggining(99)
dl.insert_at_position(90,2)
dl.insert_after_specific_item(999,99)
dl.display()
dl.delete_last()
dl.delete_first()
dl.delete_specific_item(80)
dl.delete_specific_position(2)
dl.display()



