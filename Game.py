import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.label_instruction = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
        self.label_instruction.grid(row=0, column=0, columnspan=3, pady=10)

        self.buttons = {
             "Rock": tk.Button(root, text="Rock", command=lambda: self.play("Rock")),
            "Paper": tk.Button(root, text="Paper", command=lambda: self.play("Paper")),
           "Scissors": tk.Button(root, text="Scissors", command=lambda: self.play("Scissors")),
        }

        for i, (choice, button) in enumerate(self.buttons.items()):
            button.grid(row=1, column=i, padx=10)

        self.label_result = tk.Label(root, text="")
        self.label_result.grid(row=2, column=0, columnspan=3, pady=10)

        self.label_score = tk.Label(root, text="Score: User 0 - 0 Computer")
        self.label_score.grid(row=3, column=0, columnspan=3, pady=10)

        self.button_play_again = tk.Button(root, text="Play Again", command=self.play_again, state=tk.DISABLED)
        self.button_play_again.grid(row=4, column=0, columnspan=3, pady=10)

    def play(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        result = self.determine_winner(user_choice, computer_choice)

        self.label_result.config(text=f"User: {user_choice}, Computer: {computer_choice}\n{result}")
        self.update_score(result)

        self.label_score.config(text=f"Score: User {self.user_score} - {self.computer_score} Computer")
        self.button_play_again.config(state=tk.NORMAL)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a Tie!"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Scissors" and computer_choice == "Paper") or
            (user_choice == "Paper" and computer_choice == "Rock")
        ):
            self.user_score += 1
            return "You Win!"
        else:
            self.computer_score += 1
            return "Computer Wins!"

    def update_score(self, result):
        if "Tie" not in result:
            messagebox.showinfo("Round Result", result)

    def play_again(self):
        self.label_result.config(text="")
        self.button_play_again.config(state=tk.DISABLED)

# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()