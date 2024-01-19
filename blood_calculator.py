def interface():
    print("Blood Calculator")
    print("Enter which test you want?")
    print("1 - HDL")
    print("9 - Quit")
    while True:
        choice = input("Enter your choice:")
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()
 
 
 def HDL_driver():
    print("HDL")
    HDL = get_HDL_input()
    analyse_HDL(HDL)
    output_HDL_result()
        
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

       
    
    
        
        
        
        
interface()
print("End")