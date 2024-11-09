# Shake-Roll
Shake & Roll is a multiplayer dice game designed for social gatherings, built for the Micro:Bit platform. This fun and interactive game lets players choose between 2-player and multi-player modes, allowing them to compete for the highest dice roll score. The game uses LED brightness to display player progress and winning status, adding an engaging visual element.

- Multiplayer Mode: Play with up to 25 players! Each player shakes the Micro:Bit to roll the dice, and their score is saved and displayed. The highest score is highlighted at the end.
- 2-Player Mode: Compete with one friend. Players take turns, and their progress is shown using LEDs at different brightness levels. The winner is displayed at the end.
- Intuitive Visual Feedback: LED brightness levels (50% for active players and 100% for the winner) make it easy to see each player’s status and the final result.

## Code Structure
- `show_dice(roll)`: Displays a single dice roll on the LED grid for a brief moment.
- `show_results()`: Highlights the highest scorer in multiplayer mode, with the winner shown at full brightness and total players at 50% brightness.
- Main Loop: Checks button and shake inputs to switch modes and record scores. It also handles result display based on the game mode.

## Usage

1. Start Multiplayer Mode: Press Button A, then shake the Micro:Bit to roll.
2. Start 2-Player Mode: Hold Button A for one second, and take turns shaking the Micro:Bit.
3. Display Results: In multiplayer mode, press Button B to view the results.
