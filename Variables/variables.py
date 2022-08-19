import tkinter as tk

window = tk.Tk()  # Tkinter window
window.title("Basic Calculator")  # Title of window
window.geometry("390x375")  # Dimensions / geometry of window
window.resizable(0, 0)  # Resizable window specifications (None)
text = tk.Text(master=window, height = 1, width = 15, font=("Times New Roman", 30))  # Text field (Width determines grid size)
text.grid(column=0, row=0, columnspan=4)  # Places on grid (columnspan determines how many cols textfield spans)
text.insert(tk.END, "0")  # Insert text
text.config(state=tk.DISABLED)  # Disable the state of text field (read)
calculations = ["", "", ""]  # Storage for calculations
first = True  # Determines if first number being input