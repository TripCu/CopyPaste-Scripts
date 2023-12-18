import tkinter as tk
from tkinter import scrolledtext
import pyautogui
import threading
import time
import random
import tkinter as tk
import subprocess

def run_document_writer():
    # Runs DocumentWriter.py
    subprocess.Popen(["python", "DocumentWriter.py"])

def run_main_py():
    # Runs main.py
    subprocess.Popen(["python", "main.py"])

# Create the main window
root = tk.Tk()
root.title("Script Runner")

# Create a button to run DocumentWriter.py
button_document_writer = tk.Button(root, text="Run Document Writer", command=run_document_writer, height=5, width=20)
button_document_writer.pack(pady=20)

# Create a button to run main.py
button_main_py = tk.Button(root, text="Run Main.py", command=run_main_py, height=5, width=20)
button_main_py.pack(pady=20)

root.mainloop()