import pytest

from src.person import Female, Male, Person


def test_male_get_gender():
    assert Male().get_gender() == "Male"


def test_female_get_gender():
    assert Female().get_gender() == "Female"


def test_person_is_abstract():
    with pytest.raises(TypeError):
        Person()
