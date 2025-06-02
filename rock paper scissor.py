import tkinter as tk
import random

# Game choices
choices = ["Rock", "Paper", "Scissors"]

# Function to determine the winner
def determine_winner(player_choice):
    computer_choice = random.choice(choices)
    result = ""

    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_text.set(f"Your Choice: {player_choice}\nComputer's Choice: {computer_choice}\nResult: {result}")

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.resizable(False, False)

# Display result
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 14), justify="center")
result_label.pack(pady=20)

# Buttons for choices
button_frame = tk.Frame(root)
button_frame.pack()

def create_choice_button(choice):
    return tk.Button(button_frame, text=choice, font=("Arial", 14), width=10,
                     command=lambda: determine_winner(choice))

rock_btn = create_choice_button("Rock")
paper_btn = create_choice_button("Paper")
scissors_btn = create_choice_button("Scissors")

rock_btn.grid(row=0, column=0, padx=10, pady=10)
paper_btn.grid(row=0, column=1, padx=10, pady=10)
scissors_btn.grid(row=0, column=2, padx=10, pady=10)

# Start the app
root.mainloop()
