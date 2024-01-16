import tkinter as tk
from tkinter import simpledialog
import MineSweeper_Game
   
def easy_game():
    difficulty = 1
    MineSweeper_Game.play_minesweeper(difficulty)

def medium_game():
    difficulty = 2
    MineSweeper_Game.play_minesweeper(difficulty)

def hard_game():
    difficulty = 3
    MineSweeper_Game.play_minesweeper(difficulty)

# Create the main window
root = tk.Tk()
root.title("Minesweeper Menu")

# Set the window size and position it at the center of the screen
window_width = 200
window_height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create a button to start the game
easy_button = tk.Button(root, text="Easy", command=easy_game)
easy_button.pack(pady=10)

medium_button = tk.Button(root, text="Medium", command=medium_game)
medium_button.pack(pady=10)

hard_button = tk.Button(root, text="Hard", command=hard_game)
hard_button.pack(pady=10)

# Create an exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()