import curses, random, time  # Import necessary modules for terminal control, randomness, and time
from curses import wrapper  # Import wrapper to handle curses initialization and cleanup

# List of possible strings for the typing test
choices = [
    "The quick brown fox jumped over the lazy dog while the cat watched from afar.",
    "In the early morning light, the birds sang their melodies, filling the air with joy.",
    "On a stormy night, the wind howled loudly, rattling the windows and shaking the trees outside.",
    "She packed her bags, left the city behind, and began a new adventure in the countryside.",
    "Through trials and errors, they discovered the hidden truth, buried deep beneath layers of secrecy and lies."
]

# Display the start screen
def start_screen(stdscr):
    stdscr.clear()  # Clear screen
    stdscr.addstr("Welcome to the Typing Test!")  # Display welcome message
    stdscr.addstr("\nPress any key to begin!")  # Prompt to start
    stdscr.refresh()  # Refresh screen
    stdscr.getkey()  # Wait for user input

# Display the target text and user input, highlighting correctness
def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)  # Display target text
    stdscr.addstr(1, 0, f"WPM: {wpm}")  # Display WPM on the second line

    # Display typed characters, green for correct, red for incorrect
    for i, char in enumerate(current):
        correct_char = target[i]
        if char == correct_char:
            stdscr.addstr(0, i, char, curses.color_pair(1))  # Green for correct
        else:
            stdscr.addstr(0, i, correct_char, curses.color_pair(2))  # Red for incorrect

    stdscr.refresh()  # Refresh screen to show changes

# Handle the typing test
def wpm_test(stdscr):
    target_text = random.choice(choices)  # Randomly select a target string
    current_text = []  # Store user input
    start_time = time.time()  # Record start time
    stdscr.nodelay(True)  # Enable non-blocking input

    while True:  # Loop for the typing test
        time_elapsed = max(time.time() - start_time, 1)  # Calculate elapsed time

        stdscr.clear()  # Clear screen
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)  # Calculate WPM

        display_text(stdscr, target_text, current_text, wpm)  # Display text and WPM
        str_curr_text = ''.join(current_text)  # Join user input into a string

        if str_curr_text == target_text:  # If text matches target, stop
            stdscr.nodelay(False)  # Reset blocking input
            break

        try:
            key = stdscr.getkey()  # Wait for user input
        except:
            continue  # Ignore exceptions if no input

        if ord(key) == 27:  # If Escape key is pressed, exit
            stdscr.nodelay(False)  # Reset blocking input
            break

        # Handle backspace, removing last character if present
        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):  # Add typed character if within limit
            current_text.append(key)

# Main function for initializing the test
def main(stdscr):
    # Initialize color pairs (foreground, background)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Green on black for correct input
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # Red on black for incorrect input
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # White on black

    start_screen(stdscr)  # Display start screen

    while True:
        wpm_test(stdscr)  # Start typing test

        stdscr.addstr(2, 0, "Typing test complete! Press any key to continue or ESC to exit!")  # Display completion message
        key = stdscr.getkey()  # Wait for user input to continue or exit

        if ord(key) == 27:  # If Escape key is pressed, exit
            break
        else:
            stdscr.clear()  # Clear screen for a new test

# Start the curses program, passing control to 'main'
wrapper(main)
