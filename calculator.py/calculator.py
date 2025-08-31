import tkinter as tk
from PIL import Image, ImageTk

# Function to update the input field
def on_button_click(value):
    current_text = entry_var.get()
    entry_var.set(current_text + str(value))

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Function to clear the input field
def clear():
    entry_var.set("")

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("450x320")
root.resizable(False, False)
root.configure(bg="#2c3e50")  # Dark background

icon = Image.open("calculator.py/calculator_icon.png")  # Your icon file
icon = ImageTk.PhotoImage(icon)
root.wm_iconphoto(False, icon)

# Button style
btn_bg = "#1abc9c"
btn_fg = "white"
btn_active_bg = "#16a085"

# Function to create rounded entry box using Canvas
def create_rounded_entry(row, col, width=20, height=2):
    canvas = tk.Canvas(root, width=width*20, height=height*20, bg="#2c3e50", highlightthickness=0)
    canvas.grid(row=row, column=col, columnspan=4, padx=10, pady=10, sticky="we")
    
    # Draw rounded rectangle
    radius = 10
    x0, y0, x1, y1 = 2, 2, width*20-2, height*20-2
    canvas.create_arc(x0, y0, x0+radius*2, y0+radius*2, start=90, extent=90, fill="#ecf0f1", outline="#ecf0f1")
    canvas.create_arc(x1-radius*2, y0, x1, y0+radius*2, start=0, extent=90, fill="#ecf0f1", outline="#ecf0f1")
    canvas.create_arc(x0, y1-radius*2, x0+radius*2, y1, start=180, extent=90, fill="#ecf0f1", outline="#ecf0f1")
    canvas.create_arc(x1-radius*2, y1-radius*2, x1, y1, start=270, extent=90, fill="#ecf0f1", outline="#ecf0f1")
    canvas.create_rectangle(x0+radius, y0, x1-radius, y1, fill="#ecf0f1", outline="#ecf0f1")
    canvas.create_rectangle(x0, y0+radius, x1, y1-radius, fill="#ecf0f1", outline="#ecf0f1")
    
    # Create entry widget
    entry = tk.Entry(canvas, textvariable=entry_var, font=("Arial", 20), bd=0, relief="flat", justify="right", bg="#ecf0f1")
    entry_window = canvas.create_window(width*10, height*10, window=entry)
    
    return canvas

# Entry field for calculations
entry_var = tk.StringVar()
create_rounded_entry(0, 0, width=21, height=2)

# Function to create rounded buttons using Canvas
def create_rounded_button(text, row, col, width=5, height=2):
    canvas = tk.Canvas(root, width=width*20, height=height*20, bg="#2c3e50", highlightthickness=0)
    canvas.grid(row=row, column=col, padx=5, pady=5)
    
    # Draw rounded rectangle
    radius = 10
    x0, y0, x1, y1 = 2, 2, width*20-2, height*20-2
    canvas.create_arc(x0, y0, x0+radius*2, y0+radius*2, start=90, extent=90, fill=btn_bg, outline=btn_bg)
    canvas.create_arc(x1-radius*2, y0, x1, y0+radius*2, start=0, extent=90, fill=btn_bg, outline=btn_bg)
    canvas.create_arc(x0, y1-radius*2, x0+radius*2, y1, start=180, extent=90, fill=btn_bg, outline=btn_bg)
    canvas.create_arc(x1-radius*2, y1-radius*2, x1, y1, start=270, extent=90, fill=btn_bg, outline=btn_bg)
    canvas.create_rectangle(x0+radius, y0, x1-radius, y1, fill=btn_bg, outline=btn_bg)
    canvas.create_rectangle(x0, y0+radius, x1, y1-radius, fill=btn_bg, outline=btn_bg)
    
    # Create button text
    btn_text = canvas.create_text(width*10, height*10, text=text, font=("Arial", 14), fill=btn_fg)
    
    # Bind button click
    def on_click(event):
        if text not in ["C", "="]:
            on_button_click(text)
        elif text == "C":
            clear()
        else:
            calculate()
    
    # Adjust the clickable area to be bigger but smaller than the rounded corner shape
    canvas.tag_bind(btn_text, "<Button-1>", on_click)
    canvas.tag_bind(btn_text, "<Enter>", lambda e: canvas.itemconfig(btn_text, fill=btn_active_bg))
    canvas.tag_bind(btn_text, "<Leave>", lambda e: canvas.itemconfig(btn_text, fill=btn_fg))
    canvas.tag_bind("button", "<Button-1>", on_click)
    canvas.tag_bind("button", "<Enter>", lambda e: canvas.itemconfig(btn_text, fill=btn_active_bg))
    canvas.tag_bind("button", "<Leave>", lambda e: canvas.itemconfig(btn_text, fill=btn_fg))
    
    # Create a larger clickable area
    canvas.create_rectangle(x0+radius//2, y0+radius//2, x1-radius//2, y1-radius//2, outline="", tags="button")
    
    return canvas

# Button layout
buttons = [
    ("/", 1, 0), ("*", 1, 1), ("-", 1, 2), ("+", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("C", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), (".", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("=", 4, 3),
    ("0", 5, 1)
]

# Create buttons dynamically
for text, row, col in buttons:
    create_rounded_button(text, row, col, width=5, height=2)

# Run the app
root.mainloop()