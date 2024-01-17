import tkinter as tk
import MineSweeper_Game
import json
from datetime import datetime, date

def record_score(difficulty, time_taken):
    try:
        with open('scores.json', 'r') as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = {'easy': [], 'medium': [], 'hard': []}

    scores[difficulty].append({'time': time_taken, 'date': date.today().strftime("%Y-%m-%d")})
    scores[difficulty] = sorted(scores[difficulty], key=lambda x: x['time'])[:10]

    with open('scores.json', 'w') as file:
        json.dump(scores, file, indent=2)

def show_scores():
    try:
        with open('scores.json', 'r') as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = {'easy': [], 'medium': [], 'hard': []}

    top = tk.Toplevel(root)
    top.title("Top Scores")

    for difficulty in ['easy', 'medium', 'hard']:
        label = tk.Label(top, text=f"{difficulty.capitalize()} Scores:")
        label.pack()

        for i, score in enumerate(scores[difficulty], start=1):
            time_str = f"{i}. {score['time']} seconds ({score['date']})"
            score_label = tk.Label(top, text=time_str)
            score_label.pack()

def easy_game():
    timeTaken = 0
    difficulty = 1
    timeTaken = MineSweeper_Game.play_minesweeper(difficulty)
    record_score('easy', timeTaken)

def medium_game():
    timeTaken = 0
    difficulty = 2
    timeTaken = MineSweeper_Game.play_minesweeper(difficulty)
    record_score('medium', timeTaken)

def hard_game():
    timeTaken = 0
    difficulty = 3
    timeTaken = MineSweeper_Game.play_minesweeper(difficulty)
    record_score('Hard', timeTaken)

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
easy_button.pack(pady=5)

medium_button = tk.Button(root, text="Medium", command=medium_game)
medium_button.pack(pady=5)

hard_button = tk.Button(root, text="Hard", command=hard_game)
hard_button.pack(pady=5)

scores_button = tk.Button(root, text="Show Scores", command=show_scores)
scores_button.pack(pady=5)

# Create an exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=5)

# Run the Tkinter main loop
root.mainloop()