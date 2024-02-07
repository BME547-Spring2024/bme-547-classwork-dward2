

def test_check_for_fever():
    from temperature_analysis import check_for_fever
    input_data = [98.6, 99.5, 103.1, 101.5, 80]
    answer = check_for_fever(input_data)
    expected = True
    assert answer == expected
    input_data = [98.6, 99.5, 100.1, 101.4, 80]
    answer = check_for_fever(input_data)
    expected = False
    assert answer == expected
