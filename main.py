import tkinter as tk
from tkinter import scrolledtext
import pyautogui
import threading
import time

def save_to_file():
    with open("shrek.txt", "w") as file:
        file.write(text_area.get("1.0", tk.END))
    label_status.config(text="Saved to shrek.txt")

def type_content():
    label_status.config(text="Running...")
    time.sleep(5)  # Delay before typing starts
    with open("shrek.txt", "r") as file:
        for word in file:
            pyautogui.typewrite(word)
            pyautogui.press("enter")
    label_status.config(text="Finished running")

def run_typing_sequence():
    threading.Thread(target=type_content).start()

# Create the main window
root = tk.Tk()
root.title("Copy Paster")

# Create a scrolled text area
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
text_area.pack(padx=10, pady=10)

# Create a Save button
button_save = tk.Button(root, text="Save", command=save_to_file)
button_save.pack(pady=5)

# Create a Run button
button_run = tk.Button(root, text="Run", command=run_typing_sequence)
button_run.pack(pady=5)

# Status label
label_status = tk.Label(root, text="")
label_status.pack()

# Run the application
root.mainloop()
