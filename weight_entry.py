def input_weight_entry():
    print("Enter patient weight in form of ## units (e.g., 105 lb)")
    weight_input = input("Enter weight: ")
    weight_in_kg = parse_weight_input(weight_input)
    print("The patient weight of {} kg will be stored "
          "in database.".format(weight_in_kg))


def parse_weight_input(weight_input):
    if weight_input.find(" ") < 0:
        return -1
    weight, units = weight_input.split(' ')
    weight = float(weight)
    if units.lower() in ["lb", "lbs", "pound", "pounds", "#"]:
        weight_kg = convert_lb_to_kg(weight)
    else:
        weight_kg = weight
    weight_kg = round(weight_kg)
    return weight_kg


def convert_lb_to_kg(weight_lb):
    weight_kg = weight_lb / 2.20462
    return weight_kg


def add(a, b):
    return a + b


if __name__ == "__main__":
    input_weight_entry()
