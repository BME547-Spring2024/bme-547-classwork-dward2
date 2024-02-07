def check_for_fever(input_data):
    fever_threshold = 101.5
    for temperature in input_data:
        if temperature >= fever_threshold:
            return True
    return False
