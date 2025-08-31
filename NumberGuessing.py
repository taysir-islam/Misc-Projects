import tkinter as tk
import random

font_1 = ("Arial", 24)
font_2 = ("Arial", 20)

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("750x350")

label1 = tk.Label(root, text="Welcome to the game\nI chose a number from 1 to 50 (it is an integer)", font=font_1)
label1.pack(pady=10)
label3 = tk.Label(root, text="Enter your number:", font=font_1)
label3.pack(pady=5)
entry = tk.Entry(root, font=font_2, width=8, justify='center')
entry.pack(pady=5)
entry.bind("<Return>", lambda event: check_guess())  # Submit on Enter
label2 = tk.Label(root, text="", font=font_1)
label2.pack(pady=10)

chances_label = tk.Label(root, text="Chances left: 5", font=font_1)
chances_label.pack(pady=5)

# Game state variables
random_number = random.randint(1, 50)
chances = 5

def check_guess():
    global chances, random_number
    guess = entry.get()
    if not guess.isdigit():
        label2.config(text="Please enter a valid integer.")
        entry.delete(0, tk.END)
        label1.config(text="")
        return
    user_guess = int(guess)
    if user_guess > random_number:
        chances -= 1
        label2.config(text="Too high!")
        label1.config(text="")
    elif user_guess < random_number:
        chances -= 1
        label2.config(text="Too low!")
        label1.config(text="")
    else:
        label2.config(text=f"Correct! The answer is {random_number}")
        entry.config(state='disabled')
        label1.config(text="")
        return
    chances_label.config(text=f"Chances left: {chances}")
    if chances == 0:
        label2.config(text=f"Game over! The number was {random_number}")
        entry.config(state='disabled')
        label1.config(text="")
        retry_button.pack(pady=10)
    entry.delete(0, tk.END)

def retry_game():
    global chances, random_number
    chances = 5
    random_number = random.randint(1, 50)
    label2.config(text="")
    chances_label.config(text="Chances left: 5")
    entry.config(state='normal')
    entry.delete(0, tk.END)
    retry_button.pack_forget()

retry_button = tk.Button(root, text="Retry", command=retry_game, font=font_2, width=10)
# retry_button is packed only when needed

root.mainloop()
