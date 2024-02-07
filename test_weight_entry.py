import pytest


@pytest.mark.parametrize("input, expected", [
    ("22 lb", 10),
    ("50 kg", 50),
    # ("2.2 lb", 1),
    ("22", -1),
    ("22 Lb", 10),
    ("22lb", -1),
    ("22 lbs", 10),
    ("-22 lb", -10),
    ("", -1),
    # ("ten kg", -1),

    ])
def test_parse_weight_input(input, expected):
    from weight_entry import parse_weight_input
    answer = parse_weight_input(input)
    assert answer == expected


def test_add():
    from weight_entry import add
    a = 0.1
    b = 0.2
    answer = add(a, b)
    expected = 0.3
    assert answer == pytest.approx(expected)
