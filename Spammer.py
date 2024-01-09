import tkinter as tk
from tkinter import scrolledtext
import pyautogui
import threading
import time

# Global flag to control the typing sequence
typing_active = False


def save_to_file():
    with open("SaveData.txt", "w", encoding="utf-8") as file:
        file.write(text_area.get("1.0", tk.END))
    label_status.config(text="Saved to SaveData.txt")


def type_content():
    global typing_active
    typing_active = True
    label_status.config(text="Running...")
    time.sleep(5)  # Delay before typing starts

    with open("SaveData.txt", "r", encoding="utf-8") as file:  # Ensure encoding is specified for consistency
        for line in file:
            if not typing_active:
                break
            pyautogui.typewrite(line)  # Type out the line
    label_status.config(text="Stopped" if not typing_active else "Finished running")
    typing_active = False


def run_typing_sequence():
    if not typing_active:
        threading.Thread(target=type_content, daemon=True).start()  # Make the thread a daemon so it closes with the app


def stop_typing_sequence():
    global typing_active
    typing_active = False


# Create the main window
root = tk.Tk()
root.title("Spammer")
root.config(bg='black')

# Create a scrolled text area with black background and white text
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, bg='black', fg='white')
text_area.pack(padx=10, pady=10)

# Create a Save button (yellow with black text)
button_save = tk.Button(root, text="Save", command=save_to_file, bg='yellow', fg='black')
button_save.pack(pady=5)

# Create a Run button (green with white text)
button_run = tk.Button(root, text="Run", command=run_typing_sequence, bg='green', fg='white')
button_run.pack(pady=5)

# Create a Stop button (red with white text)
button_stop = tk.Button(root, text="Stop", command=stop_typing_sequence, bg='red', fg='white')
button_stop.pack(pady=5)

# Status label
label_status = tk.Label(root, text="", bg='black', fg='white')
label_status.pack()

root.mainloop()

