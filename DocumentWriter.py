import tkinter as tk
from tkinter import scrolledtext
import pyautogui
import threading
import time
import random

# Global flag to control the typing sequence
typing_active = False


def calculate_interval(wpm):
    # Calculate the interval for a given WPM
    chars_per_minute = wpm * 5  # Average word is 5 characters
    chars_per_second = chars_per_minute / 60
    return 1 / chars_per_second  # Time between each character


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
        for line in file:
            words = line.split()
            for word in words:
                if not typing_active:
                    break

                # Randomly select a typing speed between 20 and 100 WPM
                current_wpm = random.randint(20, 100)
                interval = calculate_interval(current_wpm)

                # Type the word
                pyautogui.typewrite(word, interval=interval)
                pyautogui.press("space")

                # Increase the chance to delete and retype the word (now 30% chance)
                if random.random() < 0.3:  # 30% chance to trigger
                    # Delete the word
                    for _ in range(len(word) + 1):  # +1 for the space
                        pyautogui.press("backspace")
                    # Retype the word
                    pyautogui.typewrite(word, interval=interval)
                    pyautogui.press("space")

            if not typing_active:
                break
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
root.title("Document Writer")
root.config(bg='black')

rgb_color = (255, 0, 0)
# Create a scrolled text area with black background and white text
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, bg='black', fg='255, 0, 0')
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

# Run the application
root.mainloop()
