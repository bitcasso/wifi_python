from punkt import Punkt
from rechteck import Rechteck
from rechteck import Quadrat
import pytest

rechteck = Rechteck(Punkt(1,3),Punkt(2,5))
print(rechteck.flaeche())
print(rechteck.umfang())

quadrat = Quadrat(Punkt(1,3),5)
print(quadrat.umfang())
print(quadrat.flaeche())

