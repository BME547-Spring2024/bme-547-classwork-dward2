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
    print("HDL")
    HDL = get_HDL_input()
    HDL_level = analyse_HDL(HDL)
    output_HDL_result(HDL_level)
        
def get_HDL_input():
    HDL_value = input("Enter an HDL result: ")
    HDL_value = int(HDL_value)
    return HDL_value
    
def analyse_HDL(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value<60:
        return "Borderline Low"
    else:
        return "Low"
        
def output_HDL_result(HDL_level):
    print("The characterization of HDL is {}".format(HDL_level))

def LDL_driver():
    print("LDL")
    LDL = get_LDL_input()
    LDL_level = analyse_LDL(LDL)
    output_LDL_result(LDL_level)
        
def get_LDL_input():
    LDL_value = input("Enter an LDL result: ")
    LDL_value = int(LDL_value)
    return LDL_value
    
def analyse_LDL(LDL_value):
    if LDL_value < 130:
        return "Normal"
    elif 130 <= LDL_value < 160:
        return "Borderline High"
    elif 160 <= LDL_value < 190:
        return "High"
    else:
        return "Very High"
        
def output_LDL_result(LDL_level):
    print("The characterization of LDL is {}".format(LDL_level))

       
    
    
        
        
        
        
interface()
print("End")