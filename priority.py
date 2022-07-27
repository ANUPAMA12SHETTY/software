class priorityQEntry(object):
    def __init__(self,item,priority):
        self.item = item
        self.priority = priority

class priorityQueue:
    def __init__(self):
        self.qList = list()
    
    def isEmpty(self):
        return len(self.qList)==0
    def __len__(self):
        return len(self.qList)

    def enqueue(self,item,priority):
        entry=priorityQEntry(item,priority)
        self.qList.append(entry)

    
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        index = 0
        highest = self.qList[index].priority 
        for i in range(self.__len__()):
            if self.qList[i].priority < highest:
                highest = self.qList[i].priority
                index = i
        entry = self.qList.pop(index)
        return entry.item

def main():
    q=priorityQueue()
    q.enqueue("purple",5)
    q.enqueue("White",0)
    q.enqueue("Green",1)
    q.enqueue("Black",3)
    q.enqueue("Blue",2)
    q.enqueue("Yellow",5)
    while not q.isEmpty():
        print(q.dequeue())
        
main()