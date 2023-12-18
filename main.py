import tkinter as tk
from tkinter import scrolledtext
import pyautogui
import threading
import time

# Global flag to control the typing sequence
typing_active = False

def save_to_file():
    with open("SaveData.txt", "w") as file:
        file.write(text_area.get("1.0", tk.END))
    label_status.config(text="Saved to SaveData.txt")

def type_content():
    global typing_active
    typing_active = True
    label_status.config(text="Running...")
    time.sleep(5)  # Delay before typing starts
    with open("SaveData.txt", "r") as file:
        for word in file:
            if not typing_active:
                break
            pyautogui.typewrite(word)
            pyautogui.press("enter")
    label_status.config(text="Stopped" if not typing_active else "Finished running")
    typing_active = False

def run_typing_sequence():
    if not typing_active:
        threading.Thread(target=type_content).start()

def stop_typing_sequence():
    global typing_active
    typing_active = False

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

# Create a Stop button
button_stop = tk.Button(root, text="Stop", command=stop_typing_sequence, bg='red', fg='white')
button_stop.pack(pady=5)

# Status label
label_status = tk.Label(root, text="")
label_status.pack()

# Run the application
root.mainloop()
