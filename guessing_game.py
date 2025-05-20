import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Number Guessing Game")
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label_instruction = tk.Label(root, text="I'm thinking of a number between 1 and 100.\nCan you guess it?", font=('Arial', 14))
        self.label_instruction.pack(pady=10)

        self.entry_guess = tk.Entry(root, font=('Arial', 12))
        self.entry_guess.pack(pady=5)

        self.button_submit = tk.Button(root, text="Submit Guess", command=self.check_guess, font=('Arial', 12))
        self.button_submit.pack(pady=5)

        self.label_feedback = tk.Label(root, text="", font=('Arial', 12))
        self.label_feedback.pack(pady=10)

        self.button_reset = tk.Button(root, text="Play Again", command=self.reset_game, font=('Arial', 12))
        self.button_reset.pack(pady=5)
        self.button_reset.config(state="disabled")

    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
            self.attempts += 1

            if guess < 1 or guess > 100:
                self.label_feedback.config(text="⚠️ Enter a number between 1 and 100.")
            elif guess < self.secret_number:
                self.label_feedback.config(text="🔼 Too low! Try a higher number.")
            elif guess > self.secret_number:
                self.label_feedback.config(text="🔽 Too high! Try a lower number.")
            else:
                self.label_feedback.config(text=f"✅ Correct! You guessed it in {self.attempts} attempts.")
                self.button_submit.config(state="disabled")
                self.button_reset.config(state="normal")
        except ValueError:
            self.label_feedback.config(text="❌ Please enter a valid number.")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry_guess.delete(0, tk.END)
        self.label_feedback.config(text="")
        self.button_submit.config(state="normal")
        self.button_reset.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
