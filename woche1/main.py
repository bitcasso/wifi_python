from punkt import Punkt
from rechteck import Rechteck
from rechteck import Quadrat
import pytest

rechteck = Rechteck(Punkt(1,3),Punkt(2,5))


if __name__ == "__main__":
    quadrat = Quadrat(Punkt(1,3),5)
    print(quadrat.umfang())
    print(quadrat.flaeche())