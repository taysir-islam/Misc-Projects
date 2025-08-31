import tkinter as tk
import random

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
background_color = "#2E2E2E"  # Dark gray background color
root.configure(bg=background_color)
root.resizable(False, False)

# Label to display the winner
label = tk.Label(root, text="Winner is ...", font=("Cascadia Code", 24), bg=background_color, fg="white")
label.grid(row=4, column=0, columnspan=3)

# Create buttons for the Tic-Tac-Toe grid
a = tk.Button(root, text="__", width=10, height=4, font=("Arial", 18), bg='grey',fg='white')
a.grid(row=1, column=0)
b = tk.Button(root, text="__", width=10, height=4, font=("Arial", 18), bg='grey',fg='white')
b.grid(row=1, column=1)
c = tk.Button(root, text="__", width=10, height=4, font=("Arial", 18), bg='grey',fg='white')
c.grid(row=1, column=2)
d = tk.Button(root, text="__", width=10, height=4, font=("Arial", 18), bg='grey',fg='white')
d.grid(row=2, column=0)
e = tk.Button(root, text="__", width=10, height=4, font=("Arial", 18), bg='grey',fg='white')
e.grid(row=2, column=1)
f = tk.Button(root, text="__", width=10, height=4, font=("Arial", 18), bg='grey',fg='white')
f.grid(row=2, column=2)
j = tk.Button(root, text="__", width=10, height=4, font=("Arial", 18), bg='grey',fg='white')
j.grid(row=3, column=0)
h = tk.Button(root, text="__", width=10, height=4, font=("Arial", 18), bg='grey',fg='white')
h.grid(row=3, column=1)
i = tk.Button(root, text="__", width=10, height=4, font=("Arial", 18), bg='grey',fg='white')
i.grid(row=3, column=2)

labelspace = tk.Label(root, text="", bg=background_color,pady=5)
labelspace.grid(row=5, column=0, columnspan=3)
labelspace2 = tk.Label(root, text="", bg=background_color,pady=5)
labelspace2.grid(row=7, column=0, columnspan=3)
labelspace3 = tk.Label(root, text="", bg=background_color,pady=5)
labelspace3.grid(row=0, column=0, columnspan=3)
# Retry button to reset the game
retry = tk.Button(root, text="Retry", width=10, height=1, font=("Cascadia Code", 25), bg=background_color, fg='white',
                  command=lambda: [btn.config(text="__",fg='white', state=tk.NORMAL) for btn in buttons] +
                                  [label.config(text="Winner is ...")])
retry.grid(row=6, column=0, columnspan=3)

# List of all buttons
buttons = [a, b, c, d, e, f, j, h, i]

# Winning combinations
winning_combinations = [
    (a, b, c),
    (d, e, f),
    (j, h, i),
    (a, d, j),
    (b, e, h),
    (c, f, i),
    (a, e, i),
    (c, e, j)
]

# Function to check for a winner or a tie
def win_check():
    # Check for a winner
    for combo in winning_combinations:
        if combo[0]["text"] == combo[1]["text"] == combo[2]["text"] != "__":
            winner = combo[0]["text"]
            label.config(text=f"Winner is {winner}")
            for btn in buttons:
                btn.config(state=tk.DISABLED)
            return True

    # Check for a tie
    if all(btn["text"] != "__" for btn in buttons):
        label.config(text="It's a Tie!")
        return True

    return False

# Function for the AI's move
def ai_move():
    # Check if AI can win in the next move
    for combo in winning_combinations:
        values = [btn["text"] for btn in combo]
        if values.count("X") == 2 and values.count("__") == 1:
            combo[values.index("__")].config(text="X",fg='#ff4242')
            win_check()
            return

    # Select a random move from the available buttons
    available_buttons = [btn for btn in buttons if btn["text"] == "__"]
    if available_buttons:
        random.choice(available_buttons).config(text="X",fg='#ff4242')
        win_check()

# Function for the player's move
def player_move(button):
    if button["text"] == "__":
        button.config(text="O",fg='lightgreen')
        if not win_check():
            ai_move()

# Assign the player's move function to each button
for btn in buttons:
    btn.config(command=lambda b=btn: player_move(b))

# Run the main loop
root.mainloop()
