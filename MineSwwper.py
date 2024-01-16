import tkinter as tk
from tkinter import simpledialog
import MineSweeper_Game

#def play_minesweeper(difficulty):
    

def easy_game():
    difficulty = 1
    print(difficulty)
    
    # Call Minesweeper Game function
    #play_minesweeper(difficulty)

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
easy_button.pack(pady=20)

# Create an exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()

# Run the Tkinter main loop
root.mainloop()