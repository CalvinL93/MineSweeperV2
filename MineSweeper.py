import tkinter as tk
import MineSweeper_Game
import json
from datetime import date

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_position = (screen_width - width) // 2
    y_position = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_position}+{y_position}")

# records scores to scores.json
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

# Show scores
def show_scores():
    try:
        with open('scores.json', 'r') as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = {'easy': [], 'medium': [], 'hard': []}

    top = tk.Toplevel(root)
    top.title("Top Scores")

    # Calculate the total height needed for labels
    total_height = 30  # Initial height for the header

    for difficulty in ['easy', 'medium', 'hard']:
        total_height += 20  # Height for the difficulty label

        for score in scores[difficulty]:
            total_height += 20  # Height for each score label

    # Centers score window and adjusts height based on data
    center_window(top, 300, total_height)

    for difficulty in ['easy', 'medium', 'hard']:
        label = tk.Label(top, text=f"{difficulty.capitalize()} Scores:")
        label.pack()

        for i, score in enumerate(scores[difficulty], start=1):
            time_str = f"{i}. {score['time']} seconds ({score['date']})"
            score_label = tk.Label(top, text=time_str)
            score_label.pack()

# starts minesweeper on easy
def easy_game():
    timeTaken = 0
    difficulty = 1
    timeTaken = MineSweeper_Game.play_minesweeper(difficulty)
    record_score('easy', timeTaken)

# starts minesweeper on medium
def medium_game():
    timeTaken = 0
    difficulty = 2
    timeTaken = MineSweeper_Game.play_minesweeper(difficulty)
    record_score('medium', timeTaken)

# starts minesweeper on hard
def hard_game():
    timeTaken = 0
    difficulty = 3
    timeTaken = MineSweeper_Game.play_minesweeper(difficulty)
    record_score('hard', timeTaken)

# Create the main window
root = tk.Tk()
root.title("Minesweeper Menu")

# Set the window size and position it at the center of the screen
window_width = 200
window_height = 200

center_window(root, window_width, window_height)

# Create buttons to start the game
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