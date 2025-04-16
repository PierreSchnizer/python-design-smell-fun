import pytest
from design_smell_fun.using_slots.impl.family_tree import FamilyMember


def test_family_member():
    me = FamilyMember(family_name="Schnizer", mid_name="Begemotowitsch", first_name="Pierre")


def test_assign_slots():
    me = FamilyMember(
        family_name="Schnizer",
        mid_name="Begemotowitsch",
        first_name="Pierre"
    )
    with pytest.raises(AttributeError):
        me.birth_date = "Rosenmontag"
