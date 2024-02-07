import pytest


@pytest.mark.parametrize("input_data, expected", [
    (65, "Normal"),
    (45, "Borderline Low"),
    (20, "Low"),
    ])
def test_analyse_HDL(input_data, expected):
    from blood_calculator import analyse_HDL
    answer = analyse_HDL(input_data)
    assert answer == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-5, 5, 0),
    (-1, -1, -2),
    (10.2, 3, 13.2),
    ])
def test_add(a, b, expected):
    from blood_calculator import add
    answer = add(a, b)
    assert answer == expected


x = [1, 2, 3,]
