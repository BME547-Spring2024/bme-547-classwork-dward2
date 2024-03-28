import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("My BME 547 GUI")
    root.geometry("1000x800")

    title_label = ttk.Label(root, text="Title Label")
    title_label.grid(column=0, row=0, columnspan=2)
    other_label = ttk.Label(root, text="Other Label")
    other_label.grid(column=1, row=1)
    third_label=ttk.Label(root, text="3")
    third_label.grid(column=0, row=1)
    root.mainloop()
    print("Finished")


if __name__ == "__main__":
    main()


