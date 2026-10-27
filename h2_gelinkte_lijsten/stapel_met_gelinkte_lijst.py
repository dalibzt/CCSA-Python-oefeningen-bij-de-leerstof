class StackList:

# bij class knoop: functies push, pop, isEmpty
    class Knoop:
        def __init__(self, data=None, volgende=None):
            self.data = data
            self.volgende = volgende

    # je geeft altijd self mee als arg in de class
    def __init__(self):
        # 1 eig v stapel: is leeg
        # definieer die in constr 
        self.t = None

    def is_empty(self):
        return self.t is None
       
    def push(self, data):
        # hulp knoop maken
        hulp = StackList.Knoop(data, self.t)
        # top verleggen
        self.t = hulp

    def peek(self):
        if self.is_empty():
            return None
        return self.t.data

    def pop(self):
        if self.is_empty(): # als stapel leeg
            return None
        x = self.t.data
        self.t = self.t.volgende
        return x
        



    