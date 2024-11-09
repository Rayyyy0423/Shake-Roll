from microbit import * # using API
import random # generate dice roll for a random number from 1 to 6

# Initialize variables
player_scores = [] # to save all players' results 
max_players = 25  # Max players in multiplayer mode
players_count = 0
dual_mode = False  # Flag for dual mode

# Show dice roll at full brightness
def show_dice(roll):
    display.show(str(roll))
    sleep(500)
    display.clear()

# Show results for multiplayer mode
def show_results():
    max_score = max(player_scores)  # Get the highest score
    row, col = 0, 0
    print("Total Players Count: ", players_count)
    print("Player Score:", player_scores)
    # Show total player count at half brightness
    if players_count < max_players:
        display.set_pixel((players_count-1) % 5, (players_count-1) // 5, 5)

    # Display each player's score
    for i in range(players_count):
        # Highlight highest score at full brightness
        if player_scores[i] == max_score:
            display.set_pixel(col, row, 9)

        # Move to the next position (5 per row)
        col += 1
        if col > 4:
            col = 0
            row += 1


# Main loop
while True:
    # Hold A to enter dual mode
    if button_a.is_pressed():
        start_time = running_time()
        while button_a.is_pressed():
            if running_time() - start_time > 1000:  # Press for 1 second
                dual_mode = True
                players_count = 0
                player_scores = []
                display.clear()
                display.set_pixel(1, 2, 5)  # Left "I" at 50% brightness
                display.set_pixel(3, 2, 5)  # Right "I" at 50% brightness
                break

    # 2-player mode
    if dual_mode:
        if accelerometer.was_gesture("shake") and players_count < 2:
            roll = random.randint(1, 6)  # Generate dice roll
            show_dice(roll)
            player_scores.append(roll)
            players_count += 1

            # Update dual mode indicator
            if players_count == 1:
                display.set_pixel(3, 2, 4)
                display.set_pixel(1, 2, 9)  # Player 1 complete
            elif players_count == 2:
                display.set_pixel(1, 2, 9)
                display.set_pixel(3, 2, 9)  # Player 2 complete

            # Both players finished, show result
            if players_count == 2:
                sleep(1000)
                display.clear()
                if player_scores[0] > player_scores[1]:
                    display.show("1")  # Player 1 wins
                elif player_scores[1] > player_scores[0]:
                    display.show("2")  # Player 2 wins
                else:
                    display.show("=")  # Tie
                sleep(4000)
                display.clear()
                dual_mode = False  # Exit dual mode

    # Multi-player mode
    if button_a.was_pressed() and not dual_mode:
        display.clear()
        player_scores = []  # Clear scores
        players_count = 0  # Reset player count
        display.show(">")  # Start indicator

    # Multiplayer mode dice roll on shake
    if accelerometer.was_gesture("shake") and players_count < max_players and not dual_mode:
        roll = random.randint(1, 6)  # Generate dice roll
        show_dice(roll)
        player_scores.append(roll)
        players_count += 1

        # Show max player indicator
        if players_count == max_players:
            display.show("<")
        else:
            display.show(Image.DIAMOND)

    # Show results on B press in multiplayer mode
    if button_b.is_pressed() and players_count > 0 and not dual_mode:
        display.clear()
        show_results()
        sleep(2000)
        display.show(Image.DIAMOND)
        # display.clear()