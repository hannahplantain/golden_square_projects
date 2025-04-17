from lib.tyres import Tyres
from lib.tyres import TyreLog

"""
Given you add multiple tires
they are added to the tyres_log
"""

def test_add_1_tyre_to_the_tyres_log():
    car_tyres = TyreLog()
    tyre_1 = Tyres("Tyre 1", "front right")
    car_tyres.add(tyre_1)
    assert car_tyres.tyres_log == [tyre_1]
