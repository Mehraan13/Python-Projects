import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "#", "#", "#", "#", "O", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", "#", "#"],
    ["#", " ", "#", " ", "#", "#", " ", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"],
]

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, 'X', RED)
            else:
                stdscr.addstr(i , j*2, value, BLUE) 

def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return (i,j)


def find_path(maze, stdscr):
    start = 'O'
    end = 'X'
    start_pos = find_start(maze, start)
    
    q = queue.Queue()
    q.put((start_pos, [start_pos])) #queue will contain position and the path

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.5) # time to slow down the search
        stdscr.refresh()

        if maze[row][col] == end:
            return path
        
        neighbors = find_neighbours(maze, row, col)
        for neighbor in neighbors:
            r, c = neighbor
            if maze[r][c] == '#' or neighbor in visited:
                continue

            visited.add(neighbor)
            q.put((neighbor, path + [neighbor]))

        
def find_neighbours(maze, row, col):
    neighbours = []

    if row > 0: #up
        neighbours.append((row - 1, col))
    if row + 1 < len(maze): # down
        neighbours.append((row + 1, col))
    if col + 1 < len(maze[0]): # right
        neighbours.append((row, col + 1))
    if col > 0: # left
        neighbours.append((row, col - 1))

    return neighbours


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    
    stdscr.getch()

wrapper(main)