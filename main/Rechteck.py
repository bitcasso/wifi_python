from .punkt import Punkt

class Rechteck:

    p1 = 0
    p2 = 0

    def __init__(self, p1: Punkt, p2: Punkt):
        self.p1 = p1
        self.p2 = p2

    def flaeche(self):
        laenge, breite = self.laengen()
        return laenge * breite

    def umfang(self):
        laenge, breite = self.laengen()
        return 2*(laenge+breite)
    
    def laengen(self):
        return  abs(self.p1.x - self.p2.x), abs(self.p2.y - self.p1.y)

class Quadrat(Rechteck):
    def __init__(self,punkt1, groesse) :
        self.p1 = punkt1
        self.p2 = Punkt(punkt1.x + groesse, punkt1.y + groesse)

