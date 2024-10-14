import tkinter as tk

def move_forward():
    print("Moving Forward")

def move_backward():
    print("Moving Backward")

def move_left():
    print("Moving Left")

def move_right():
    print("Moving Right")

def move_forward_left():
    print("Moving Forward Left")

def move_forward_right():
    print("Moving Forward Right")

def move_backward_left():
    print("Moving Backward Left")

def move_backward_right():
    print("Moving Backward Right")

def turn_left():
    print("Turning Left")

def turn_right():
    print("Turning Right")

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

# Arrange buttons in a grid
forward_button.grid(row=0, column=1, pady=5)
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