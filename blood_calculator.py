def interface():
    print("Blood Calculator")
    print("Enter which test you want?")
    print("1 - HDL")
    print("2 - LDL")
    print("9 - Quit")
    while True:
        choice = input("Enter your choice:")
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
 
 
def HDL_driver():
    test_name = "HDL"
    HDL = get_input(test_name)
    HDL_level = analyse_HDL(HDL)
    output_result(test_name, HDL_level)
        
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

def LDL_driver():
    test_name = "LDL"
    LDL = get_input(test_name)
    LDL_level = analyse_LDL(LDL)
    output_result(test_name, LDL_level)
        
def analyse_LDL(LDL_value):
    if LDL_value < 130:
        return "Normal"
    elif 130 <= LDL_value < 160:
        return "Borderline High"
    elif 160 <= LDL_value < 190:
        return "High"
    else:
        return "Very High"
        
        
interface()
print("End")