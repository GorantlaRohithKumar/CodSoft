import tkinter as tk
import random

# Function to determine the winner of the game
def determine_winner(user_choice):
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    
    if user_choice == computer_choice:
        result_label.config(text=f'Tie! Computer also chose {computer_choice}')
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result_label.config(text=f'You win! Computer chose {computer_choice}')
    else:
        result_label.config(text=f'You lose! Computer chose {computer_choice}')

# Create a tkinter window
window = tk.Tk()
window.title('Rock, Paper, Scissors Game')

# Create labels and buttons
instruction_label = tk.Label(window, text='Select Rock, Paper, or Scissors:')
instruction_label.pack()

rock_button = tk.Button(window, text='Rock', command=lambda: determine_winner('Rock'))
paper_button = tk.Button(window, text='Paper', command=lambda: determine_winner('Paper'))
scissors_button = tk.Button(window, text='Scissors', command=lambda: determine_winner('Scissors'))

rock_button.pack()
paper_button.pack()
scissors_button.pack()

result_label = tk.Label(window, text='')
result_label.pack()

# Start the tkinter main loop
window.mainloop()
