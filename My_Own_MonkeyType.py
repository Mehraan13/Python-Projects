import curses, random, time  # Import the curses module for terminal control and random module for random selection
from curses import wrapper  # Import the wrapper function to handle curses initialization and cleanup

# List of possible strings for the typing test
choices = [
    "The quick brown fox jumped over the lazy dog while the cat watched from afar.",
    "In the early morning light, the birds sang their melodies, filling the air with joy.",
    "On a stormy night, the wind howled loudly, rattling the windows and shaking the trees outside.",
    "She packed her bags, left the city behind, and began a new adventure in the countryside.",
    "Through trials and errors, they discovered the hidden truth, buried deep beneath layers of secrecy and lies."
]

# Function to display the start screen
def start_screen(stdscr):
    stdscr.clear()  # Clear any existing content from the terminal screen
    stdscr.addstr("Welcome to the Typing Test!")  # Add the welcome message at the top of the screen
    stdscr.addstr("\nPress any key to begin!")  # Prompt user to press any key to start the test
    stdscr.refresh()  # Refresh the screen to display the updated content
    stdscr.getkey()  # Wait for user input (any key) before proceeding


def display_text(stdscr, target, current, wpm = 0):
    
    stdscr.addstr(target)  # Display the target text on the screen
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    # Loop through the typed characters and display them in a different color
    for i, char in enumerate(current):
        correct_char = target[i]
        if char == correct_char:
            stdscr.addstr(0, i, char, curses.color_pair(1))  # Display each typed character in green
        else:
            stdscr.addstr(0, i, correct_char, curses.color_pair(2))

    stdscr.refresh()  # Refresh the screen to show changes

# Function to handle the typing test
def wpm_test(stdscr):
    target_text = random.choice(choices)  # Randomly select a string from the 'choices' list as the target text
    current_text = []  # List to store the characters the user has typed
    wpm = 0
    start_time = time.time() #stores seconds pass an epoch
    stdscr.nodelay(True)

    while True:  # Infinite loop to keep the typing test running until the user exits
        time_elapsed = max(time.time() - start_time, 1) #max is used to avoid zero division error on first iteration

        stdscr.clear()  # Clear the screen at the start of each loop iteration
        
        wpm = round((len(current_text) / (time_elapsed/60)) / 5) #wpm

        display_text(stdscr, target_text,current_text, wpm)
        
        stdscr.refresh()  # Refresh the screen to show changes
        str_curr_text = ''.join(current_text)

        if str_curr_text == target_text:
            stdscr.nodelay(False) #stop waiting for user input
            break

        try: #due to stdscr no delay this throws an exception
            key = stdscr.getkey()  # Wait for user input (key press)
        except:
            continue 

        if ord(key) == 27:
            stdscr.nodelay(False)  # ASCII value 27 represents the Escape key, exit the loop if pressed
            break

        # Handle backspace key (KEY_BACKSPACE, '\b', '\x7f' are common representations of backspace)
        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text) > 0:  # Ensure there's something to delete
              current_text.pop()  # Remove the last typed character
        elif len(current_text) < len(target_text):
            current_text.append(key)  # Add the pressed key to the current text

# Define the main function where curses settings and test initialization take place
def main(stdscr):
    # Define color pairs for use in the program (foreground, background)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Green on black
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # Red on black
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # White on black 

    start_screen(stdscr)  # Display the start screen
    
    while True:
        wpm_test(stdscr)  # Start the typing test

        stdscr.addstr(2, 0, "Typing test complete! Press any key to continue!")

        key = stdscr.getkey()
        if ord(key) == 27:
            break
        else:
            stdscr.clear()
    
# Call the wrapper function to handle curses environment setup and pass control to 'main' function
wrapper(main)
