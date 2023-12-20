import tk
inter as tk
import subprocess
from tkinter import font as tkFont  # Importing tkinter font module


def run_document_writer():
    # Runs DocumentWriter.py
    subprocess.Popen(["python", "DocumentWriter.py"])


def run_Spammer_py():
    # Runs main.py
    subprocess.Popen(["python", "Spammer.py"])


# Create the main window
root = tk.Tk()
root.title("Script Runner")
root.config(bg='black')  # Set background color of the root window

# Define a bold and white font
bold_font = tkFont.Font(family="Helvetica", size=12, weight="bold")

# Create a button to run DocumentWriter.py
button_document_writer = tk.Button(root, text="Run Document Writer", command=run_document_writer, height=5, width=20,
                                   bg='black', fg='white', font=bold_font)
button_document_writer.pack(pady=20)

# Create a button to run main.py
button_main_py = tk.Button(root, text="Run Spammer", command=run_Spammer_py, height=5, width=20, bg='black', fg='white',
                           font=bold_font)
button_main_py.pack(pady=20)

root.mainloop()
