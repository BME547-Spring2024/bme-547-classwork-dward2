import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk


def process_donor(user_name, id_number, blood_letter, rh_factor,
                  donation_center):
    if user_name == "":
        return "No donor name entered.  Nothing saved."
    if id_number == "":
        return "No id number entered.  Nothind saved."
    print("Donor, Id: {}, {}".format(user_name, id_number))
    print("Blood Type: {}{}".format(blood_letter, rh_factor))
    print("Donation Center: {}".format(donation_center))
    return "Donor Saved"


def load_and_size_image(filename):
    raw_pil_image = Image.open(filename)
    print(raw_pil_image.size)
    final_width = 100
    final_height = 100
    alpha_x = final_width / raw_pil_image.size[0]
    alpha_y = final_height / raw_pil_image.size[1]
    alpha = min(alpha_x, alpha_y)
    new_x = round(raw_pil_image.size[0] * alpha)
    new_y = round(raw_pil_image.size[1] * alpha)
    pil_image = raw_pil_image.resize((new_x, new_y))
    return pil_image


def main():

    def cancel_btn_cmd():
        choice = messagebox.askyesno("Verify Close", "Are you sure you want "
                                                     "to exit.")
        if choice == tk.YES:
            root.destroy()

    def ok_btn_cmd():
        # Get data from the GUI
        name_input = name_data.get()
        id_input = id_data.get()
        blood_letter = blood_type.get()
        rh_factor = rh_value.get()
        dc_input = dc_choice.get()
        # Call an external, testable function that receives GUI Data and
        #    returns an answer
        result = process_donor(name_input, id_input, blood_letter, rh_factor,
                               dc_input)
        # Update the GUI as needed
        result_label.configure(text=result)

    def image_select_cmd():
        # Get data from GUI
        filename = filedialog.askopenfilename(initialdir=".")
        if filename == "":
            return
        # Call external functions to do the work
        pil_image = load_and_size_image(filename)
        # Update GUI
        tk_image = ImageTk.PhotoImage(pil_image)
        image_label.configure(image=tk_image)
        image_label.image = tk_image

    # Create root window
    root = tk.Tk()
    root.title("Blood Donor Database")
    # root.geometry("1000x800")

    # Create title, name and id widgets
    title_label = ttk.Label(root, text="Blood Donor Database")
    title_label.grid(column=0, row=0, columnspan=2, sticky=tk.W)
    name_label = ttk.Label(root, text="Name:")
    name_label.grid(column=0, row=1, sticky=tk.E)
    name_data = tk.StringVar()
    # name_data.set("Enter your name here")
    name_entry = ttk.Entry(root, textvariable=name_data)
    name_entry.grid(column=1, row=1, sticky=tk.W)
    id_label = ttk.Label(root, text="ID:")
    id_label.grid(column=0, row=2, sticky=tk.E, pady=5)
    id_data = tk.StringVar()
    id_entry = ttk.Entry(root, textvariable=id_data)
    id_entry.grid(column=1, row=2, sticky=tk.W, pady=5)

    # Create label to use for GUI output
    result_label = ttk.Label(root)
    result_label.grid(column=1, row=5, columnspan=2, sticky=tk.W)

    # Create widgets for rH factor
    rh_value = tk.StringVar()
    rh_value.set("-")
    rh_checkbox = ttk.Checkbutton(root, text="rH positive", onvalue="+",
                                  offvalue="-", variable=rh_value)
    rh_checkbox.grid(column=1, row=4)

    # Create widgets for blood type letter
    blood_type = tk.StringVar()
    a_btn = ttk.Radiobutton(root, text="A", variable=blood_type, value="A")
    a_btn.grid(column=0, row=3, sticky=tk.W)
    b_btn = ttk.Radiobutton(root, text="B", variable=blood_type, value="B")
    b_btn.grid(column=0, row=4, sticky=tk.W)
    ab_btn = ttk.Radiobutton(root, text="AB", variable=blood_type, value="AB")
    ab_btn.grid(column=0, row=5, sticky=tk.W)
    o_btn = ttk.Radiobutton(root, text="O", variable=blood_type, value="O")
    o_btn.grid(column=0, row=6, sticky=tk.W)

    # Create Combobox Widgets
    dc_label = ttk.Label(root, text="Closest Donation Center")
    dc_label.grid(column=2, row=0, sticky=tk.W, padx=5)
    dc_choice = tk.StringVar()
    dc_locations = ("Durham", "Orange", "Wake")
    dc_entry = ttk.Combobox(root, values=dc_locations,
                            textvariable=dc_choice, state='readonly')
    dc_entry.grid(column=2, row=1, sticky=tk.W, padx=5)

    # Create image widgets
    filename = "avatar.jpg"
    pil_image = load_and_size_image(filename)
    tk_image = ImageTk.PhotoImage(pil_image)
    image_label = ttk.Label(root, image=tk_image)
    image_label.image = tk_image
    image_label.grid(column=3, row=0, rowspan=5)

    image_select_btn = ttk.Button(root, text="Select Picture",
                                  command=image_select_cmd)
    image_select_btn.grid(column=4, row=0)

    # Create button widgets
    cancel_btn = ttk.Button(root, text="Cancel", command=cancel_btn_cmd)
    cancel_btn.grid(column=2, row=6)
    ok_btn = ttk.Button(root, text="Ok", command=ok_btn_cmd)
    ok_btn.grid(column=1, row=6)

    root.mainloop()
    print("Finished")


if __name__ == "__main__":
    main()
