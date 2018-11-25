class Station:

    def __init__(self, name = None, n = None, p = None, isTrans = None):
        self.name = name
        self.n = n
        self.p = p
        self.isTrans = isTrans

        if isTrans:
            self.n1 = None
            self.p1 = None


class Line:

    def __init__(self, station):
        self.head = station
        self.currentStation = self.head

    def append(self, nextStation):
        self.currentStation.n = nextStation
        nextStation.p = self.currentStation
        self.currentStation = nextStation

    def count(self, startStation, endStation):
        c = 0
        this = self.head
        while this.name != startStation:
            this = this.n
        while this.name != endStation:
            this = this.n
            c += 1
        return c


line1List = ['Mohammad Naguib', 'Sadat', 'Opera', 'Dokki']
line1 = Line(Station('Ataba'))
for element in line1List:
    line1.append(Station(element))

print(line1.head.name)
print(line1.currentStation.name)
print(line1.count('Dokki', 'Sadat'))