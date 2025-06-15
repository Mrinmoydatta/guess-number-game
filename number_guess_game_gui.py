import tkinter as tk
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label_title = tk.Label(root, text="Guess a number between 1 and 100", font=("Helvetica", 14))
        self.label_title.pack(pady=20)

        self.entry = tk.Entry(root, font=("Helvetica", 14), justify='center')
        self.entry.pack(pady=10)

        self.button_check = tk.Button(root, text="Check", command=self.check_guess, font=("Helvetica", 12))
        self.button_check.pack()

        self.label_result = tk.Label(root, text="", font=("Helvetica", 12))
        self.label_result.pack(pady=10)

        self.label_attempts = tk.Label(root, text="Attempts: 0", font=("Helvetica", 10))
        self.label_attempts.pack()

        self.button_restart = tk.Button(root, text="Restart Game", command=self.restart_game, font=("Helvetica", 10))
        self.button_restart.pack(pady=10)

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.label_result.config(text="Enter a valid number!", fg="red")
            return

        guess = int(guess)
        self.attempts += 1
        self.label_attempts.config(text=f"Attempts: {self.attempts}")

        if guess < self.secret_number:
            self.label_result.config(text="Too low!", fg="blue")
        elif guess > self.secret_number:
            self.label_result.config(text="Too high!", fg="orange")
        else:
            self.label_result.config(text=f"Correct! You guessed it in {self.attempts} tries.", fg="green")

    def restart_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.label_result.config(text="")
        self.label_attempts.config(text="Attempts: 0")
        self.entry.delete(0, tk.END)

# Creating window and run
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
