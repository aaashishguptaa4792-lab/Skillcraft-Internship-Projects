# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 17:01:59 2026

@author: ASHISH
"""

import tkinter as tk
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Quest")
        self.root.configure(bg="#f0f8ff") 

        self.secret_number = None
        self.attempts = 0
        self.best_score = None

        # Title
        self.label_title = tk.Label(root, text="🎮Mystery Number Quest !", font=("Arial", 14), bg="#f0f8ff")
        self.label_title.pack(pady=10)

        # Difficulty selection
        self.label_diff = tk.Label(root, text="Select Difficulty:", font=("Arial", 12), bg="#f0f8ff")
        self.label_diff.pack(pady=5)

        self.diff_var = tk.StringVar(value="Medium")
        self.combo_diff = tk.OptionMenu(root, self.diff_var, "Easy", "Medium", "Hard")
        self.combo_diff.pack(pady=5)

        # Entry field
        self.entry_guess = tk.Entry(root, width=10, font=("Arial", 12))
        self.entry_guess.pack(pady=5)

        # Button
        self.btn_check = tk.Button(root, text="Check Guess", command=self.check_guess, bg="#add8e6")
        self.btn_check.pack(pady=5)

        # Result label
        self.label_result = tk.Label(root, text="", font=("Arial", 12), bg="#f0f8ff")
        self.label_result.pack(pady=10)

        # Scoreboard
        self.label_scoreboard = tk.Label(root, text="Best Score: None", font=("Arial", 12), fg="blue", bg="#f0f8ff")
        self.label_scoreboard.pack(pady=10)

        # Replay button
        self.btn_replay = tk.Button(root, text="Play Again", command=self.reset_game, bg="#add8e6")
        self.btn_replay.pack(pady=5)

        # Start first game
        self.reset_game()

    def set_range(self):
        difficulty = self.diff_var.get()
        if difficulty == "Easy":
            return 50
        elif difficulty == "Medium":
            return 100
        elif difficulty == "Hard":
            return 500

    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
            self.attempts += 1

            if guess == self.secret_number:
                self.label_result.config(text=f"🎉 Correct! Attempts: {self.attempts}")
                if self.best_score is None or self.attempts < self.best_score:
                    self.best_score = self.attempts
                    self.label_scoreboard.config(text=f"Best Score: {self.best_score} attempts 🏆")
                else:
                    self.label_scoreboard.config(text=f"Best Score: {self.best_score} attempts")
            elif guess < self.secret_number:
                self.label_result.config(text="Too low! Try again.")
            else:
                self.label_result.config(text="Too high! Try again.")
        except ValueError:
            self.label_result.config(text="Invalid input! Enter a number.")

    def reset_game(self):
        max_number = self.set_range()
        self.secret_number = random.randint(1, max_number)
        self.attempts = 0
        self.entry_guess.delete(0, tk.END)
        self.label_result.config(text=f"New game started! Range: 1–{max_number}")

# Run the game
root = tk.Tk()
game = GuessingGame(root)
root.mainloop()
