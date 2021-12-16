class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = []
        self.fillInList(nestedList)
    
    def fillInList(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                self.list.append(item.getInteger())
            else:
                self.fillInList(item.getList())
    
    def next(self) -> int:
        if self.hasNext():
            return self.list.pop(0)
        return -1
        
    l
    def hasNext(self) -> bool:
         return len(self.list) > 0