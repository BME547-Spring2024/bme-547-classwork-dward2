def interface():
    print("Blood Calculator")
    print("Enter which test you want?")
    print("1 - HDL")
    print("2 - LDL")
    print("3 - Total Cholesterol")
    print("9 - Quit")
    while True:
        choice = input("Enter your choice:")
        if choice == "9":
            return
        elif choice == "1":
            driver("HDL")
        elif choice == "2":
            driver("LDL")
        elif choice == "3":
            driver("Total Cholesterol")
 
 
def driver(test_name):
    value = get_input(test_name)
    function_to_call = None
    if test_name == "HDL":
        function_to_call = analyse_HDL
    elif test_name == "LDL":
        function_to_call = analyse_LDL
    elif test_name == "Total Cholesterol":
        function_to_call = analyse_total_chol
    level = function_to_call(value)
    output_result(test_name, level)
        
def get_input(test_name):
    test_value = input("Enter an {} result: ".format(test_name))
    test_value = int(test_value)
    return test_value
    
def analyse_HDL(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value<60:
        return "Borderline Low"
    else:
        return "Low"
        
def output_result(test_name, HDL_level):
    print("The characterization of {} is {}".format(test_name, HDL_level))

def analyse_LDL(LDL_value):
    if LDL_value < 130:
        return "Normal"
    elif 130 <= LDL_value < 160:
        return "Borderline High"
    elif 160 <= LDL_value < 190:
        return "High"
    else:
        return "Very High"
        
def analyse_total_chol(LDL_value):
    if LDL_value < 200:
        return "Normal"
    elif 200 <= LDL_value < 240:
        return "Borderline High"
    else:
        return "High"
        
interface()
print("End")