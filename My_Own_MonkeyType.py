import curses, random  # Import the curses module for controlling terminal output
from curses import wrapper  # Import the wrapper function from curses to manage initialization and cleanup

choices = [
    "The quick brown fox jumped over the lazy dog while the cat watched from afar.",
    "In the early morning light, the birds sang their melodies, filling the air with joy.",
    "On a stormy night, the wind howled loudly, rattling the windows and shaking the trees outside.",
    "She packed her bags, left the city behind, and began a new adventure in the countryside.",
    "Through trials and errors, they discovered the hidden truth, buried deep beneath layers of secrecy and lies."
]



def start_screen(stdscr):
    stdscr.clear()  # Clear the terminal screen to remove any existing content
    stdscr.addstr("Welcome to the Typing Test!")  # Add the string "Hello world!" to coordinates 0,0 at the current cursor position (default: top-left)
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()  # Refresh the terminal to display the added string
    stdscr.getkey()
    
def wpm_test(stdscr):
    target_text = random.choice(choices)
    current_text = []

    while True:
        stdscr.clear()
        stdscr.addstr(target_text)

        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))

        stdscr.refresh()

        key = stdscr.getkey()
        
        if ord(key) == 27: #ascii of escape
            break
        if key in ("KEY_BACKSPACE", '\b', '\x7f'): #representation of backspace
            if len(current_text) > 0:
                current_text.pop()
        else:   
            current_text.append(key)

# Define the main function that will handle the terminal output
def main(stdscr):
    #color pairs for referencing later
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)
    
# Call the wrapper function, which initializes the curses environment and passes control to the main function
wrapper(main)
