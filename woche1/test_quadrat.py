from woche1 import Rechteck
from woche1 import Punkt
import pytest

# Arrange
@pytest.fixture
def rechteck():
    return Rechteck(Punkt(0,5), Punkt(5,10))

def test_flaeche(rechteck: Rechteck):
    assert(rechteck.flaeche() == 25)

def test_umfang(rechteck: Rechteck):
    assert(rechteck.umfang() == 20)