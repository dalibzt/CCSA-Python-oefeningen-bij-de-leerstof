class HashSet:
    FLAG = 99999
    def __init__(self, max_size=10):
        self.container = [None]*max_size
        self.max_size = max_size


    def add(self, item):
        if self.index_of(item)!= -1:
            return -1
        # item toevoegen
        h = hash(item)
        # hoe hash passen in de hashset met max lengte 0-9
        index = h % self.max_size
        begin = index
        # contr of plaats leeg
        while self.container[index] != None and self.container[index] != HashSet.FLAG:
            print(index)
            #                 modulo
            index = (index +1) % self.max_size
            if index == begin:
                raise ValueError("container is vol")
        self.container[index]
        return index
        

    def index_of(self, item):
        h = hash(item)
        index = h % self.max_size
        begin = index
        while index is not None and self.container[index] != item:
            # 1 opschuiven in de set
            index = (index+1) % self.max_size
            if index == begin:
                return -1
        if self.container == item:
            return index
        return -1

    def delete(self, item):
        # de self arg moet je niet meer meegeven omdat self. er al is
        index = self.index_of(item)
        if index == -1:
            return False
        else:
            self.container[index] = HashSet.FLAG
            return True
        


    





