import tkinter as tk
from PIL import Image, ImageTk # Pillow (PythonImagingLibrary fork)

import class_motor_control


# import class_motor_control



def move_forward():
    print("Moving Forward")
    # class_motor_control.forward()

def move_backward():
    print("Moving Backward")
    # class_motor_control.backward()

def move_left():
    print("Moving Left")
    # class_motor_control.left()

def move_right():
    print("Moving Right")
    # class_motor_control.right()

def move_forward_left():
    print("Moving Forward Left")
    # class_motor_control.forward_left()

def move_forward_right():
    print("Moving Forward Right")
    # class_motor_control.forward_right()

def move_backward_left():
    print("Moving Backward Left")
    # class_motor_control.backward_left()

def move_backward_right():
    print("Moving Backward Right")
    # class_motor_control.backward_right()

def turn_left():
    print("Turning Left")
    # class_motor_control.turn_left()

def turn_right():
    print("Turning Right")
    # class_motor_control.turn_right()

def show_help():
    help_window = tk.Toplevel(root)
    help_window.title("Help")
    img = Image.open("mecanum_directions.png")
    img = img.resize((925, 790), Image.LANCZOS) # resampling filter high-quality downsampling
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(help_window, image=photo)
    label.image = photo  # Keep a reference to prevent garbage collection
    label.pack()

# Create the main window
root = tk.Tk()
root.title("Mecanum-Robot-Car Remote-Control")

# Create buttons
forward_button = tk.Button(root, text="^\nForward", width=15, background="magenta", command=move_forward)
backward_button = tk.Button(root, text="Backward\nv", width=15, background="magenta", command=move_backward)
left_button = tk.Button(root, text="< Left", width=15, background="magenta", command=move_left)
right_button = tk.Button(root, text="Right >", width=15, background="magenta", command=move_right)
forward_left_button = tk.Button(root, text="Forward Left", width=15, command=move_forward_left)
forward_right_button = tk.Button(root, text="Forward Right", width=15, command=move_forward_right)
backward_left_button = tk.Button(root, text="Backward Left", width=15, command=move_backward_left)
backward_right_button = tk.Button(root, text="Backward Right", width=15, command=move_backward_right)
turn_left_button = tk.Button(root, text="Turn Left", width=15, command=turn_left)
turn_right_button = tk.Button(root, text="Turn Right", width=15, command=turn_right)
help_button = tk.Button(root, text="Help", width=10, command=show_help)

# Arrange buttons in a grid
forward_button.grid(row=0, column=1, pady=5)
help_button.grid(row=0, column=2, padx=5, pady=5, sticky='ne')
forward_left_button.grid(row=1, column=0, padx=5)
forward_right_button.grid(row=1, column=2, padx=5)
left_button.grid(row=2, column=0, padx=5)
right_button.grid(row=2, column=2, padx=5)
backward_left_button.grid(row=3, column=0, padx=5, pady=(0, 0))
turn_left_button.grid(row=4, column=0, padx=5, pady=(0, 0))
backward_right_button.grid(row=3, column=2, padx=5, pady=(0, 0))
turn_right_button.grid(row=4, column=2, padx=5, pady=(0, 0))
backward_button.grid(row=5, column=1, pady=5)

# Start the GUI event loop
root.mainloop()