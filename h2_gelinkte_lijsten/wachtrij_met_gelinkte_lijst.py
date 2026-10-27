class QueueList:

    class Knoop:

        def __init__(self,data=None,volgende=None) -> None:
            self.data = data
            self.volgende = volgende


    def __init__(self) -> None:
        # lege Kop en staart
        self.k = None
        self.s = None

    def is_empty(self):
        if self.is_empty():
            self.k = self.hulp
            self.s = self.hulp
        return self.K is None

    def enqueue(self,data):
        hulp = QueueList.Knoop(data, self.t)
        x = hulp.data
        if self.is_empty(): #ben ni zeker over deze if
            self.k = hulp
            self.s = hulp
        else :
            self.s.volgende = hulp
            self.s = hulp


    def front(self):
        return self.k.data

    def dequeue(self):
        if self.is_empty():
            return None
        if self.k == self.s:
            x = self.k.data
            self.k, self.s = None
        else:
            self.k = self.k.volgende
        return x


    def invert(self):
        #keert wachtrij om
        vorige = None
        #pijl verleggen
        ref = self.k
        while ref is not None:
            volgende = ref.volgende
            ref.volgende = vorige # hier draai ik de pijl om v rechts nr links
            vorige = ref # vorige schuift door
            ref = volgende # ref schuift door
        self.k, self.s = self.s, self.k
